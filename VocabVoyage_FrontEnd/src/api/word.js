import myAxios from "../request.js";

// 单词模糊搜索
export const wordFuzzySearch = async (params) => {
    const res = await myAxios.request({
        url: "/word/search?query=" + params,
        method: "GET"
    });
    return res;
}


// 根据单词 id 获取单词信息
export const getWordById = async (id) => {
    const res = await myAxios.request({
        url: "/word/" + id,
        method: "GET"
    });
    return res;
}


// 根据单词拼写获取单词信息
export const getWordBySpell = async (spell) => {
    const res = await myAxios.request({
        url: "/word/?word_spell=" + spell,
        method: "GET"
    })
    return res;
}


// 根据记忆结果更新单词熟练度
export const memorizeWord = async (params) => {
    const res = await myAxios.request({
        url: "/word/memorize",
        method: "POST",
        data: params
    })
    return res;
}


// 获取学习单词
export const getLearningWord = async (params) => {
    const res = await myAxios.request({
        url: "/word/list/by/proficiency",
        method: "POST",
        data: params
    })
    return res;
}