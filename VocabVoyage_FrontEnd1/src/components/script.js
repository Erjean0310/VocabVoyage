// 获取页面元素
const phoneInput = document.getElementById('phone');
const passwordInput = document.getElementById('password');
const rememberMeCheckbox = document.getElementById('rememberMe');
const loginButton = document.getElementById('loginButton');

// 页面加载时自动填充保存的值
window.onload = () => {
    const savedPhone = localStorage.getItem('phone');
    const savedPassword = localStorage.getItem('password');
    const isRemembered = localStorage.getItem('rememberMe') === 'true';

    if (isRemembered) {
        phoneInput.value = savedPhone || '';
        passwordInput.value = savedPassword || '';
        rememberMeCheckbox.checked = true;
    }
};

loginButton.addEventListener('click', () => {
    const phone = phoneInput.value;
    const password = passwordInput.value;
    const isRememberMeChecked = rememberMeCheckbox.checked;

    if (isRememberMeChecked) {
        // 保存电话号码和密码
        localStorage.setItem('phone', phone);
        localStorage.setItem('password', password); // 安全性低，实际应用中建议加密处理
        localStorage.setItem('rememberMe', 'true');
    } else {
        // 清除保存的数据
        localStorage.removeItem('phone');
        localStorage.removeItem('password');
        localStorage.setItem('rememberMe', 'false');
    }

    // 模拟登录逻辑
    alert('登录成功！');
});
