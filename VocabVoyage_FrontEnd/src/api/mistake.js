import myAxios from "../request.js";

// 获取出错单词列表
export const searchMistakeList = async (params) => {
    const res = await myAxios.request({
        url: "/mistake/list",
        method: "POST",
        data: params

    });
    return res;
}

// 上报单词错误
export const wordMistakeReport = async (params) => {
    const res = await myAxios.request({
        url: "/mistake/report",
        method: "POST",
        data: params

    });
    return res;
}


