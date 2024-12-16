<template>
  <div class="calendar-container">
    <!-- 日历容器 -->
    <div class="calendar-header">
      <!-- 日历顶部，显示年份、月份和切换按钮 -->
      <button @click="changeMonth(-1)">上一月</button>
      <h3>{{ currentYear }}年{{ currentMonth + 1 }}月</h3>
      <button 
        @click="changeMonth(1)" 
        :disabled="isCurrentMonth"
        :class="{ disabled: isCurrentMonth }"
      >
        下一月
      </button>
    </div>
    <div class="calendar-grid">
      <!-- 显示星期名称 -->
      <div class="day-label" v-for="(day, index) in weekDays" :key="index">{{ day }}</div>
      <!-- 显示当月所有日期及其签到状态 -->
      <div
        v-for="day in daysInMonth"
        :key="day.date"
        :class="['calendar-day', { signed: day.signed }]"
      >
        {{ day.day }}
      </div>
    </div>
  </div>
</template>

<script>
import { getUserSigninRecord } from '../api/user.js';

export default {
  data() {
    return {
      currentYear: new Date().getFullYear(), // 当前年份
      currentMonth: new Date().getMonth(),  // 当前月份（0-11）
      signedDays: [], // 保存已签到的日期
      weekDays: ["日", "一", "二", "三", "四", "五", "六"], // 星期标签
    };
  },
  computed: {
    // 计算当月显示的所有天数（包含前导空白格子）
    daysInMonth() {
      const days = [];
      // 当月第一天是星期几
      const firstDayOfMonth = new Date(this.currentYear, this.currentMonth, 1).getDay();
      // 当月最后一天的日期（例如31号）
      const lastDateOfMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();

      // 填充空白前导格子
      for (let i = 0; i < firstDayOfMonth; i++) {
        days.push({ day: "", signed: false });
      }

      // 填充当月的天数
      for (let day = 1; day <= lastDateOfMonth; day++) {
        const dateString = `${this.currentYear}-${this.currentMonth + 1}-${day}`; // 格式化日期字符串
        days.push({
          day, // 日期数字
          date: dateString, // 完整日期字符串
          signed: this.signedDays.includes(dateString), // 检查是否已签到
        });
      }

      return days;
    },
    // 检查当前是否为当前真实月份
    isCurrentMonth() {
      const today = new Date();
      return this.currentYear === today.getFullYear() && this.currentMonth === today.getMonth();
    },
    // 当前月份的字符串格式（YYYY-MM）
    currentMonthString() {
      return `${this.currentYear}-${String(this.currentMonth + 1).padStart(2, '0')}`;
    },
  },
  methods: {
    // 获取指定月份的签到数据
    async fetchSignedDays() {
      try {
        // 请求后端 API，返回当前月份已签到的日期
        const response = await fetch(`/api/signed-days?month=${this.currentMonthString}`);
        if (!response.ok) {
          throw new Error("Failed to fetch signed days");
        }
        const data = await response.json();
        this.signedDays = data.signedDays || []; // 更新已签到的日期
      } catch (error) {
        console.error("Error fetching signed days:", error);
      }
    },
    // 切换月份（前一月或后一月）
    changeMonth(direction) {
      this.currentMonth += direction; // 修改当前月份
      if (this.currentMonth < 0) {
        this.currentMonth = 11; // 如果是1月切换到前一月，则年份减1
        this.currentYear -= 1;
      } else if (this.currentMonth > 11) {
        this.currentMonth = 0; // 如果是12月切换到下一月，则年份加1
        this.currentYear += 1;
      }
      this.fetchSignedDays(); // 切换月份后重新获取签到数据
    },
    async fetchUserSigninRecord() {
      try {
        const response = await getUserSigninRecord('2024-12'); // 传入所需的参数
        if (response.data.code === 1) {
          this.signedDays = response.data.data; // 将返回的签到日期保存到 signedDays
        }
      } catch (error) {
        console.error("获取签到记录失败:", error);
      }
    },
  },
  mounted() {
    this.fetchSignedDays(); // 初始化组件时获取当月签到数据
    this.fetchUserSigninRecord();
  },
};
</script>

<style scoped>
.calendar-container {
  width: 100%;
  max-width: 480px; /* 增大日历容器宽度 */
  margin: 0 auto;
  text-align: center;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  padding-right: 50px;
  background-color: #f9f9f9;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr); /* 每行7格 */
  gap: 8px; /* 网格之间的间距 */
}

.day-label {
  font-weight: bold;
  color: #555;
}

.calendar-day {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 50%; /* 将日期单元格设置为圆形 */
  text-align: center;
  width: 24px; /* 固定宽度 */
  height: 24px; /* 固定高度，保证为正圆 */
  line-height: 24px; /* 文本垂直居中 */
  margin: 0 auto; /* 居中显示 */
}

.calendar-day.signed {
  background-color: #4caf50; /* 已签到的背景色 */
  color: white; /* 已签到的文字颜色 */
  border-color: #4caf50; /* 已签到的边框颜色 */
}

.calendar-day:hover {
  background-color: #f0f0f0; /* 鼠标悬浮时的背景色 */
}

button.disabled {
  background-color: #ccc; /* 禁用按钮的背景色 */
  cursor: not-allowed; /* 禁用状态的鼠标样式 */
}
</style>