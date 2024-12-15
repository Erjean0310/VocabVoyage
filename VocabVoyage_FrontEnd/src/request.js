import axios from "axios";

const myAxios = axios.create({
    baseURL: "http://localhost:8000",
    timeout: 10000,
    withCredentials: true,
});

// Add a request interceptor
myAxios.interceptors.request.use(
    function (config) {
        // Do something before request is sent
        return config;
    },
    function (error) {
        // Do something with request error
        return Promise.reject(error);
    }
);

// Add a response interceptor
myAxios.interceptors.response.use(
    function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data
        console.log(response);

        const { data } = response;
        console.log(data);
        // 未登录
        if (data.code === 40100) {
            // 不是获取用户信息接口，或者不是登录页面，则跳转到登录页面  TODO 修改
            if (
                !response.request.responseURL.includes("user/current") &&
                !window.location.pathname.includes("/user/login")
            ) {
                window.location.href = `/user/login?redirect=${window.location.href}`;
            }
        }
        return response;
    },
    function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        return Promise.reject(error);
    }
);

export default myAxios;


// import axios from 'axios'
//
// //创建一个axios对象出来
// const request = axios.create({
//     baseURL: "http://127.0.0.1:8000",//TODO最后改成实际url
//     timeout: 5000,
//     withCredentials: true
// });
//
// //request拦截器
// request.interceptors.request.use(config => {
//     config.headers['Content-Type'] = 'application/json;charset=utf-8';
//
//     return config;
// }, error => {
//     return Promise.reject(error)
// });
//
// //response拦截器
// request.interceptors.response.use(
//     response=>{
//         let res;
//         res = response.data;
//
//         if(typeof res === 'string'){
//             res = res ? JSON.parse(res) : res;
//         }
//         return res;
//     },
//     error => {
//         console.log('err' + error);
//         return Promise.reject(error);
// })
//
// export default request;
//
