<script setup>
import { ref } from 'vue';
// 这里可以按需引入头像图片地址，如果是使用默认图标样式则可以不引入具体图片资源
const avatarUrl = ref('https://example.com/your-avatar.jpg'); // 示例图片地址，替换成真实的图片路径或链接
const data = ref({
    name: '111',
    radio: '12345@qq.com',
    checkbox: [],
    select: '',
    multipleSelect: [],
    // 为原密码、新密码、确认密码分别设置不同的变量
    oldPassword: '1234',
    newPassword: '',
    confirmPassword: '',
    phone: '120110'
});

const add = () => {
    // 打印数据，实际应用中可以进行数据验证等操作
    console.log(data.value);
    // 关闭对话框
    dialog.value = false;
};

const reset = () => {
    data.value = {
        name: '',
        radio: '',
        checkbox: [],
        date: '',
        select: '',
    multipleSelect: [],
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
    };
    // 关闭对话框
    dialog.value = false;
};

// 对话框
const dialog = ref(false);

const dialogClose = () => {
    console.log("关闭");
};
</script>

<template>
    <div class="info-text">基本信息</div>
    <avatar
      :src="avatarUrl"
      size="large"
      class="avatar-style bg-gray-circle"
    ></avatar>
    <div class="user-info" style="margin-left: 550px; margin-top: -140px;">用户个人信息</div>
    <div class="user-detail">
        <div style="margin-bottom: 23px;">账号名：{{ data.name }}</div>
        <div style="margin-bottom: 23px;">手机号：(+86){{ data.phone }}</div>
        <div style="margin-bottom: 23px;">邮件地址：{{ data.radio }}</div>
        <div style="margin-bottom: 40px;">密码：{{ data.oldPassword }}
            <el-button @click="dialog = true" style="margin-top: 0px; font-size: 20px; margin-left: 320px; background-color: #409EFF; /* 设置按钮背景色为Element Plus默认的蓝色 */
    border: none; /* 去除边框 */
    color: white;">重置</el-button>
        </div>
    </div>
    <hr style="margin-left: 550px; margin-top: 10px; width: 1500px; border: none; border-top: 1px solid #ccc;">
    <div class="progress-info">用户进度信息</div>
    <div class="user-detail-extra">
        <div style="margin-bottom: 23px;">开通时间：<span style="margin-left: 10px; font-size: 23px; color: #808080;">2024/04/19 14:32:37 GMT+08:00</span></div>
        <div style="margin-bottom: 23px;">姓名：{{ data.name }}</div>
        <div style="margin-bottom: 23px;">认证信息：<span style="margin-left: 10px; font-size: 23px; color: #808080;">在校学生</span></div>
        <div style="margin-bottom: 23px;">联系地址：<span style="margin-left: 10px; font-size: 23px; color: #808080;">中国湖北省武汉市洪山区湖北省武汉市武汉理工大学南湖校区 430070</span></div>
        <div style="margin-bottom: 23px;">所背词书：<span style="margin-left: 10px; font-size: 23px; color: #808080;">六级词书</span></div>
    </div>
    <hr style="margin-left: 550px; margin-top: 30px; width: 1500px; border: none; border-top: 1px solid #ccc;"> <!-- 调整此处的 margin-top 与用户进度信息一致 -->
    <div>
        <div class="progress-info" style="margin-left: 550px; margin-top: 30px;">关闭个人信息</div>
        <el-button type="primary" class="close-btn" style="margin-left: 550px; margin-top: 40px; font-size: 20px; border-radius: 5px; padding: 5px 50px; width: 200px;">关闭</el-button> <!-- 增加距离、拉长按钮 -->
    </div>
    <!-- draggable 允许拖拽 -->
    <el-dialog v-model="dialog" width="700" title="修改密码" draggable @close="dialogClose">
        <el-form label-width="100">
            <el-form-item label="手机号："  style="margin-bottom: 20px; font-size: 35px; ">
                <el-input v-model="data.name" placeholder="请填写手机号" style="font-size: 23px;" disabled />
        </el-form-item>

            <el-form-item label="原密码：" style="margin-bottom: 20px; font-size: 35px;">
                <el-input v-model="data.oldPassword" placeholder="请填写原密码" style="font-size: 23px;" disabled />
            </el-form-item>

            <el-form-item label="新密码：" style="margin-bottom: 20px; font-size: 35px;">
                <el-input v-model="data.newPassword" placeholder="请填写新密码" class="large-font" style="font-size: 23px;" />
            </el-form-item>

            <el-form-item label="请确认：" style="margin-bottom: 30px; font-size: 35px;">
                <el-input v-model="data.confirmPassword" placeholder="请再次填写新密码" style="font-size: 23px;" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="add" style="margin-left: auto; margin-right: 20px; font-size: 23px;">确认</el-button>
                <el-button @click="reset" style="margin-left: auto; margin-right: 200px; font-size: 23px;">取消</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<style scoped>
.info-text {
    margin-left: 50px;
    margin-top: 50px;
    font-family: Arial, sans-serif;
    font-size: 30px;
    color: #000; /* 设置为黑色 */
}

.avatar-style {
    margin-left: 180px;
    margin-top: 80px;
    font-family: Arial, sans-serif;
    font-size: 30px;
}

.bg-gray-circle {
    background-color: gray;
    border-radius: 50%;
    width: 140px;
    height: 140px;
}
.large-label-font {
    font-size: 40px;
}
.user-info {
    font-family: Arial, sans-serif;
    font-size: 30px;
    color: #000; /* 设置为黑色 */
}

.user-detail {
    margin-left: 550px;
    margin-top: 30px;
    font-family: Arial, sans-serif;
    font-size: 23px;
    color: #808080;
}

.progress-info {
    margin-left: 550px;
    margin-top: 30px;
    font-family: Arial, sans-serif;
    font-size: 30px;
    color: #000; /* 设置为黑色 */
}

.user-detail-extra {
    margin-left: 550px;
    margin-top: 30px;
    font-family: Arial, sans-serif;
    font-size: 23px;
    color: #808080;
}

/* 调整 el-dialog 内文字大小以及输入框样式 */
el-dialog {
    font-size: 24px;
    color: #000; /* 设置为黑色 */
}

el-form-item label {
    font-size: 45px;
    color: #000; /* 设置为黑色 */
}

el-input {
    width: 400px;
    font-size: 35px;
    margin-left: 20px; /* 让输入框往右移一点 */
    color: #000; /* 设置为黑色 */
}

.close-btn {
    background-color: #409EFF; /* 设置按钮背景色为Element Plus默认的蓝色 */
    border: none; /* 去除边框 */
    color: white; /* 设置文字颜色为白色 */
    /* 拉长按钮 */
    padding: 5px 50px;
    width: 200px;
}
</style>