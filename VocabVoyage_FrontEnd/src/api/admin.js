import myAxios from "../request.js";

//检查管理员身份
export const adminCheck = async () => {
    const res = await myAxios.request({
        url: "/admin/check/status",
        method: "Get",
        // data: params,
    });
    return res;
}

//管理员导出数据库数据
export const adminExportData = async (params) => {
    const res = await myAxios.request({
        url: "/admin/export/data",
        method: "Put",
        data: params,
    });
    return res;
}



// // 注册
// export const userRegister = async (params) => {
//     const res = await myAxios.request({
//         url: "/user/register",
//         method: "POST",
//         data: params,
//     });
//     return res;
// }


// // 登录
// export const userLogin = async (params) => {
//     const res = await myAxios.request({
//         url: "/user/login",
//         method: "POST",
//         data: params
//     });
//     return res;
// }


// // 登出
// export const userLogout = async () => {
//     const res = await myAxios.request({
//         url: "/user/logout",
//         method: "POST"
//     });
//     return res;
// }


// // 修改密码
// export const changePassword = async (params) => {
//     const res = await myAxios.request({
//         url: "/user/change/password",
//         method: "POST",
//     })
// }



// // 签到
// export const userSignIn = async () => {
//     const res = await myAxios.request({
//         url: "/user/sign/in",
//         method: "PUT",
//     })
//     return res;
// }


// // 检查当前用户是否已经签到
// export const userCheckSignInStatus = async (params) => {
//     const res = await myAxios.request({
//         url: "/user/sign/in/status",
//         method: "GET",
//     });
//     return res;
// }

// // 获取个人信息
// export const getUserInfo = async () => {
//     const res = await myAxios.request({
//         url: "/user/me",
//         method: "GET",
//     })
//     return res;
// }