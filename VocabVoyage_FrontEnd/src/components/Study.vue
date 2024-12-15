<template>
    <div>
        <!-- 顶部区域 -->
        <div class="top">
            <div class="search">
                <div class="searchicon"></div>
                <div class="searchbox">
                    <form @submit.prevent="onSearch">
                        <input style="width: 75%;height: 40px;border-radius: 15px;" type="text" v-model="searchQuery" placeholder="">
                    </form>
                </div>
            </div>
            <div class="user">
                <div id="usericon" @click="toggleUserBox"></div>
                <div v-show="userBoxVisible" id="userbox">
                    <input type="text" v-model="username" placeholder="Enter your username"><br>
                    <input type="password" v-model="password" placeholder="Enter your password">
                    <div id="submit" @click="submitUser">Submit</div>
                    <p id="output">{{ output }}</p>
                </div>
            </div>
            <div class="calendar">
                <div id="calendaricon" @click="toggleCalendarBox"></div>
                <div v-show="calendarBoxVisible" id="calendarbox"></div>
            </div>
        </div>

        <!-- 中间区域 -->
        <div class="middle">
            <div>
                <div class="article">
                    <h1>文章标题</h1>
                    <p class="text">{{ articleText }}</p>
                </div>
                <div id="worddetail" v-show="wordDetailVisible">
                    <!-- 详细信息 -->
                </div>
            </div>
            <div id="words" class="words">
                <ul>
                    <li v-for="(word, index) in words" :key="index">
                        <div class="wordbox" @click="showWordDetail(word)">
                            <div class="word">{{ word.text }}</div>
                            <div class="playPauseBtn fas fa-play-circle" @click.stop="playAudio(word.audioSrc)"></div>
                            <audio class="audio" :src="word.audioSrc"></audio>
                            <div class="get"></div>
                            <div class="describe">{{ word.description }}</div>
                        </div>
                    </li>
                </ul>
            </div>

            <!-- 进度条 -->
            <div class="progressbar">
                <span id="bar" :style="{ width: progressBarWidth }"></span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const searchQuery = ref('');
const username = ref('');
const password = ref('');
const output = ref('');
const userBoxVisible = ref(false);
const calendarBoxVisible = ref(false);
const wordDetailVisible = ref(false);
const progressBarWidth = ref('0%');

const articleText = ref('A little panda picks up a pumpkin and wants to take it home. But the pumpkin is too big. The panda can\'t take it home.');

const words = ref([
    { text: 'cancel', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=cancel', description: 'vt.取消，注销，抵消，偿还，〈数〉约去' },
    { text: 'explosive', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=explosive', description: 'adj.爆炸的，易爆炸的，突增的，暴躁的' },
    { text: 'numerous', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=numerous', description: 'adj.很多的，许多的，数量庞大的数量庞大的，数不清的' },
    { text: 'govern', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=govern', description: 'vt.统治，管理，治理，支配（词或短语的形式或用法）' },
    { text: 'analyse', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=analyse', description: 'vt.分析，分解，细察na。“analyze”的变体' },
    { text: 'discourage', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=discourage', description: 'vt.使气馁，使沮丧，阻碍，劝阻' },
    { text: 'resemble', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=resemble', description: 'vt.与…相像，类似于' },
    { text: 'remote', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=remote', description: 'adj.（时间上）遥远的，远离的，远程的，微小的' },
    { text: 'salary', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=salary', description: 'n.薪水，薪金，薪俸' },
    { text: 'pollution', audioSrc: 'http://dict.youdao.com/dictvoice?type=1&audio=pollution', description: 'n.污染（作用），腐败，堕落，沾污' },
]);

const toggleUserBox = () => {
    userBoxVisible.value = !userBoxVisible.value;
};

const toggleCalendarBox = () => {
    calendarBoxVisible.value = !calendarBoxVisible.value;
};

const submitUser = () => {
    // 处理用户提交
    alert('Submitting user data...');
};

const onSearch = () => {
    // 处理搜索
    alert(`Searching for: ${searchQuery.value}`);
};

const playAudio = (audioSrc) => {
    const audio = new Audio(audioSrc);
    audio.play();
};

const showWordDetail = (word) => {
    // 显示单词详细信息
    alert(`Showing details for: ${word.text}`);
};
</script>

<style scoped>
.top {
    position: relative;
    height: 40px;
    margin-top: 30px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    justify-content: center;
}

.search {
    position: absolute;
    display: inline-block;
    width: 80%;
    height: 40px;
}

.searchicon {
    position: absolute;
    display: inline-block;
    width: 20%;
    font-family: 'icomoon';
    font-size: 35px;
    line-height: 40px;
    margin-top: 4px;
    color: #5F6368;
}

.searchbox {
    display: inline-block;
    position: absolute;
    width: 80%;
    margin-left: 45px;
    height: 40px;
}

.user {
    display: inline-block;
    position: absolute;
    width: 20%;
    font-family: 'icomoon';
    font-size: 35px;
    line-height: 40px;
    margin-left: 63%;
    color: darkgray;
}

.calendar {
    display: inline-block;
    position: absolute;
    width: 20%;
    font-family: 'icomoon';
    font-size: 35px;
    line-height: 40px;
    margin-left: 71%;
    color: darkgray;
}

#usericon {
    display: inline-block;
    margin-left: auto;
    margin-right: auto;
    cursor: pointer;
}

#calendaricon {
    display: inline-block;
    position: absolute;
    width: 20%;
    font-family: 'icomoon';
    font-size: 35px;
    line-height: 40px;
    margin-left: 30%;
    color: darkgray;
    cursor: pointer;
}

#userbox {
    display: none;
    position: absolute;
    width: 170%;
    height: 600px;
    margin-left: -155%;
    margin-top: 10%;
    background-color: lightgray;
    border-radius: 8px;
    z-index: 1000;
    opacity: 0;
    box-shadow: 2px 2px 15px gray;
}

#calendarbox {
    display: none;
    position: absolute;
    width: 250%;
    height: 400px;
    margin-left: -200%;
    margin-top: 30%;
    background-color: lightgray;
    border-radius: 8px;
    z-index: 1000;
    opacity: 0;
    box-shadow: 2px 2px 15px gray;
}

.middle {
    position: relative;
    height: 600px;
    margin-top: 5px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 20px;
}

.article {
    position: absolute;
    display: inline-flexbox;
    width: 65%;
    height: 80%;
    margin-left: 30px;
    margin-top: 30px;
    overflow-y: scroll;
    border-radius: 20px;
    background-color: #F1F1F1;
}

.words {
    position: absolute;
    display: inline-block;
    width: 30%;
    height: 90%;
    margin-left: 70%;
    margin-top: 30px;
    background-color: #F0F2F4;
    overflow-y: auto;
    border-radius: 20px;
}

.progressbar {
    position: absolute;
    width: 40%;
    height: 20px;
    background-color: gainsboro;
    margin-left: 10%;
    margin-top: 550px;
    border-radius: 10px;
}

#bar {
    position: absolute;
    width: 0%;
    height: 100%;
    border-radius: 10px;
    background-color: #93ADE3;
    cursor: pointer;
    transition: width 0.5s ease;
}
</style>