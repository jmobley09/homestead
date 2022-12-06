import api from "../../api";
import _ from "lodash";

export default function () {
  return {
    namespaced: true,
    state: {
        data: {},
    },
    getters: {
        categories: (state) => state.data.categories,
    },
    mutations: {
      beginLoading(state) {
        state.loading = true;
      },
      endLoading(state) {
        state.loading = false;
      },
      setInitialized(state) {
        state.initialized = true;
      },
      serverResponse(state, response) {
        state.data = response.data;
      },
    },
    actions: {
      initialize({ commit, getters, dispatch, state }) {
        if (!state.initialized) {
          commit("setInitialized");
          dispatch("request");
        }
      },
      request({ commit }) {
        commit("beginLoading");
        let url = `localhost:8081/categories`;
        api
          .get(url)
          .then((response) => commit("serverResponse", response))
          .finally((_) => commit("endLoading"));
      },
    },
  };
}
