// // import myAxios from "../request.js";
// //
// //
// // // 大模型对话
// // export const modelChat = async (params) => {
// //     const res = await myAxios.request({
// //         url: "/model/chat",
// //         method: "POST",
// //         data: params,
// //         headers: {
// //             "Content-Type": "application/json"
// //         }
// //     });
// //     return res;
// // }
//
//
//
// import myAxios from "../request.js";
// import marked from 'marked'; // 确保marked库已经被正确导入
//
// // 大模型对话
// export const modelChat = async (newMessage, messages) => {
//     if (newMessage.trim()) {
//         const userMessage = marked(newMessage);
//         messages.push({ role: 'user', content: userMessage });
//         newMessage = '';
//
//         try {
//             const response = await myAxios.request({
//                 url: "/model/chat",
//                 method: "POST",
//                 data: { messages },
//                 headers: {
//                     "Content-Type": "application/json"
//                 }
//             });
//
//             if (response.status === 200) {
//                 const assistantMessage = response.data; // 假设后端返回的是一个字符串
//                 messages.push({ role: 'assistant', content: assistantMessage, streaming: true });
//                 messages[messages.length - 1].streaming = false;
//             } else {
//                 console.error('Error:', response.status);
//             }
//         } catch (error) {
//             console.error('Error:', error);
//         }
//     }
// }