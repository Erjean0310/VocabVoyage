import myAxios from "../request.js";

// 注册
export const userRegister = async (params) => {
    const res = await myAxios.request({
        url: "/user/register",
        method: "POST",
        data: params,
    });
    return res;
}


// 登录
export const userLogin = async (params) => {
    const res = await myAxios.request({
        url: "/user/login",
        method: "POST",
        data: params
    });
    return res;
}


// 登出
export const userLogout = async () => {
    const res = await myAxios.request({
        url: "/user/login",
        method: "POST"
    });
    return res;
}


// 修改密码
export const changePassword = async (params) => {
    const res = await myAxios.request({
        url: "/user/change/password",
        method: "POST",
    })
}



// 签到
export const userSignIn = async () => {
    const res = await myAxios.request({
        url: "/user/sign/in",
        method: "GET",
    })
    return res;
}


// 检查当前用户是否已经签到
export const userCheckSignInStatus = async (params) => {
    const res = await myAxios.request({
        url: "/user/sign/in/status",
        method: "GET",
    });
    return res;
}

// 获取个人信息
export const getUserInfo = async () => {
    const res = await myAxios.request({
        url: "/user/me",
        method: "GET",
    })
    return res;
}