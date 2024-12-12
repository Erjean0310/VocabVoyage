<template>
  <div id="app">
    <Header />
    <MainContent />
  </div>
  <MarkdownViewer :markdownContent="markdownData" />
</template>

<script>
import { ref } from 'vue'
import MarkdownViewer from './components/MarkdownViewer.vue'


export default {
  components: {
    MarkdownViewer
  },
  setup() {
    const markdownData = ref(`
#  MySQL

---

**关系型数据库(RDBMS)**;建立在关系模型基础上，由多张二维表组成的数据库。

**数据模型**:客户端------>DBMS(数据库管理系统)----SQL语句----->数据库
## 一、SQL


---

### DDL（数据定义语言）
\`show databases;\`   **--展示所有数据库**

\`select database();\`  -**-查询当前所在数据库**

\`create database [if not exists] 数据库名 [字符集] [排序规则];\`  **--创建新数据库**

drop database [if exists] 数据库名; **--删除数据库**

\`use 数据库名;\`  **--使用数据库;**

\`show tables;\` -**-查询当前数据库所有表**

\`desc 表名;\` **--查询表结构**

\`show create table\` 表名; -**- 查询指定表创建时语句**
    `)

    return { markdownData }
  }
}
</script>
