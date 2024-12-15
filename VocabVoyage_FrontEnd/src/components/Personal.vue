<script setup>
import { ref } from 'vue';
import router from '../router';
const avatarUrl = ref('http://vocab-voyage.oss-cn-beijing.aliyuncs.com/kk.jpg'); // 示例图片地址,替换成真实的图片路径或链接
const data = ref({
    name: '110',
    radio: '12345@qq.com',
    checkbox: [],
    select: '',
    multipleSelect: [],
    oldPassword: '1234',
    newPassword: '',
    confirmPassword: '',
    phone: '110'
});

const add = () => {
    console.log(data.value);
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
    dialog.value = false;
};

const dialog = ref(false);

const dialogClose = () => {
    console.log("关闭");
};
</script>

<template>
    <div class="container">
        <div class="info-text">基本信息</div>
        <div class="avatar-container">
            <avatar :src="avatarUrl" size="large" class="avatar-style bg-gray-circle"></avatar>
            <div class="user-info">用户个人信息</div>
        </div>
        <div class="user-detail">
            <div>账号名：{{ data.name }}</div>
            <div>手机号：(+86){{ data.phone }}</div>
            <div>邮件地址：{{ data.radio }}</div>
            <div>密码：{{ data.oldPassword }}
                <el-button @click="dialog = true" class="reset-btn">重置</el-button>
            </div>
        </div>
        <hr>
        <div class="progress-info">用户进度信息</div>
        <div class="user-detail-extra">
            <div>开通时间：<span>2024/04/19 14:32:37 GMT+08:00</span></div>
            <div>姓名：{{ data.name }}</div>
            <div>认证信息：<span>在校学生</span></div>
            <div>联系地址：<span>中国湖北省武汉市洪山区湖北省武汉市武汉理工大学南湖校区 430070</span></div>
            <div>所背词书：<span>六级词书</span></div>
        </div>
        <hr>
        <div class="close-btn-container">
            <div class="progress-info">关闭个人信息</div>
            <el-button type="primary" class="close-btn">关闭</el-button>
        </div>
        <el-dialog v-model="dialog" width="700" title="修改密码" draggable @close="dialogClose">
            <el-form label-width="100">
                <el-form-item label="手机号：">
                    <el-input v-model="data.name" placeholder="请填写手机号" disabled />
                </el-form-item>

                <el-form-item label="原密码：">
                    <el-input v-model="data.oldPassword" placeholder="请填写原密码" disabled />
                </el-form-item>

                <el-form-item label="新密码：">
                    <el-input v-model="data.newPassword" placeholder="请填写新密码" />
                </el-form-item>

                <el-form-item label="请确认：">
                    <el-input v-model="data.confirmPassword" placeholder="请再次填写新密码" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="add">确认</el-button>
                    <el-button @click="reset">取消</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.info-text {
    font-size: 1.5rem;
    color: #000;
}

.avatar-container {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.avatar-style {
    background-color: gray;
    border-radius: 50%;
    width: 100px;
    height: 100px;
}

.user-info {
    font-size: 1.5rem;
    color: #000;
    margin-left: 20px;
}

.user-detail,
.user-detail-extra {
    font-size: 1rem;
    color: #808080;
    margin-top: 20px;
}

.user-detail div,
.user-detail-extra div {
    margin-bottom: 10px;
}

hr {
    margin: 20px 0;
    border: none;
    border-top: 1px solid #ccc;
}

.progress-info {
    font-size: 1.5rem;
    color: #000;
}

.close-btn-container {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-top: 20px;
}

.close-btn {
    margin-left: 20px;
}

.reset-btn {
    margin-left: 10px;
    font-size: 1rem;
    padding: 5px 10px;
}

el-dialog {
    font-size: 1rem;
    color: #000;
}

el-form-item label {
    font-size: 1rem;
    color: #000;
}

el-input {
    width: 100%;
    font-size: 1rem;
    color: #000;
}
</style>