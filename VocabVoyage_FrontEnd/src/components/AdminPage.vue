
<template>
    <div style="padding: 20px;">
        <el-table :data="mistakeData" style="width: 100%">
            <el-table-column prop="mistake_id" label="ID" width="50" />
            <el-table-column prop="word_spell" label="出错单词" width="180" />
            <el-table-column prop="word_meaning" label="词义" width="400" />
            <el-table-column prop="reporter_nick_name" label="报告人" width="120" />
            <el-table-column prop="report_time" label="报告时间" width="180" />
            <el-table-column prop="status" label="状态" width="100" />
            <el-table-column prop="word_description" label="详细描述" width="700">
                <template v-slot="scope">
                    <el-button @click="toggleDetails(scope.row)">
                        {{ scope.row.showDetails ? '隐藏详细内容' : '显示详细内容' }}
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-pagination
            v-model:current-page="pageNumber"
            v-model:page-size="pageSize"
            :page-sizes="[5, 10, 50, 100]"
            layout="total, sizes, prev, pager, next, jumper"
            :total="totalNumber"
            @current-change="handleSearch"
            @size-change="handleSearch"
        />
        <el-button type="primary" @click="handleExportData">保存数据库中的文件</el-button>
        <div v-if="selectedMistake">
            <el-card class="detail-card">
                <div v-html="selectedMistake.word_description"></div>
            </el-card>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { searchMistakeList } from "../api/mistake";

const pageNumber = ref(1);
const pageSize = ref(10);
const totalNumber = ref(0);
const mistakeData = ref([{
      "mistake_id": 3,
      "word_spell": "AIDS",
      "word_meaning": " 爱滋病,获得性免疫功能丧失综合症(Acquired Immure Deficiency Syndrome)",
      "word_description": "### 分析词义\n\n  \n\n*   AIDS（Acquired Immune Deficiency Syndrome）是一种由病毒（特别是HIV病毒）引发的疾病，翻译成中文就是\"获得性免疫缺陷综合症\"。HIV病毒会破坏人体的免疫系统，使得患者对其他疾病很难抵抗。\n\n  \n\n### 列举例句\n\n  \n\n1.  Many people living with AIDS encounter discrimination in all aspects of their lives. 许多患有艾滋病的人在生活的各个方面都会遭受歧视。\n2.  He's doing research on the treatment of AIDS. 他正在研究艾滋病的治疗方法。\n3.  The government launched a nationwide campaign to prevent the spread of AIDS. 政府发起了一场全国性的防止艾滋病传播的运动。\n\n  \n\n### 词根分析\n\n  \n\n*   AIDS是一个缩写形式的词，它的全称是 Acquired Immune Deficiency Syndrome, 其中 \"acquired\" 的词根是 \"acquir-\" 来源于拉丁语 \"acquirere\"，意思是 \"得到\"；\"Immune\" 的词根是 \"immun-\"，来自于拉丁语 \"immunis\"，意思是 \"免疫的\"；\"deficiency\" 的词根是 \"defic-\" 来源于拉丁语 \"deficere\"，意思是 \"缺乏\"；\"syndrome\" 的词根是 \"syn-\" 和 \"drome\" 两部分，\"syn-\" 来源于古希腊语，意为 \"合并\"，\"drome\" 来自古希腊，意为 \"奔跑\"，它整体表示的是一系列的症状。\n\n  \n\n### 词缀分析\n\n  \n\n*   AIDS是一个缩写词，由四个不同的词组成，所以并没有词缀。\n\n  \n\n### 发展历史和文化背景\n\n  \n\n*   AIDS 在1981年当时被镶嵌出来，这被公认为历史上第一个被诊断出来的艾滋病病例。这个词首次被美国食品和药物管理局（FDA）和美国疾病控制和预防中心（CDC）提出并广泛接受。\n\n  \n\n### 单词变形\n\n  \n\n*   AIDS 作为疾病的名字，是一个命名词，，没有变型。但是，请注意这个单词在口语中常常全部使用大写（AIDS）。\n\n  \n\n### 记忆辅助\n\n  \n\n*   由于AIDS是由四个英文单词的首字母组成的缩写，所以记忆AIDS，最好是记住这四个单词：Acquired, Immune, Deficiency, Syndrome，然后再将这四个单词的含义串连起来。\n\n  \n\n### 小故事\n\n  \n\nIn a small town, everyone knew Tom had AIDS. Despite the disease, Tom never lost his optimism and continued to help others, becoming an inspiration to those around him. 生活在小镇上的每个人都知道Tom得了艾滋病。尽管有了这个疾病，Tom从未丧失乐观的态度，他继续帮助他人，成为周围人的灵感来源。",
      "reporter_nick_name": "nick_name3",
      "solver_nick_name": null,
      "report_time": "2024-12-13T21:19:26",
      "resolved_time": null,
      "status": "未解决"
    },
    {
      "mistake_id": 4,
      "word_spell": "AIDS",
      "word_meaning": " 爱滋病,获得性免疫功能丧失综合症(Acquired Immure Deficiency Syndrome)",
      "word_description": "### 分析词义\n\n  \n\n*   AIDS（Acquired Immune Deficiency Syndrome）是一种由病毒（特别是HIV病毒）引发的疾病，翻译成中文就是\"获得性免疫缺陷综合症\"。HIV病毒会破坏人体的免疫系统，使得患者对其他疾病很难抵抗。\n\n  \n\n### 列举例句\n\n  \n\n1.  Many people living with AIDS encounter discrimination in all aspects of their lives. 许多患有艾滋病的人在生活的各个方面都会遭受歧视。\n2.  He's doing research on the treatment of AIDS. 他正在研究艾滋病的治疗方法。\n3.  The government launched a nationwide campaign to prevent the spread of AIDS. 政府发起了一场全国性的防止艾滋病传播的运动。\n\n  \n\n### 词根分析\n\n  \n\n*   AIDS是一个缩写形式的词，它的全称是 Acquired Immune Deficiency Syndrome, 其中 \"acquired\" 的词根是 \"acquir-\" 来源于拉丁语 \"acquirere\"，意思是 \"得到\"；\"Immune\" 的词根是 \"immun-\"，来自于拉丁语 \"immunis\"，意思是 \"免疫的\"；\"deficiency\" 的词根是 \"defic-\" 来源于拉丁语 \"deficere\"，意思是 \"缺乏\"；\"syndrome\" 的词根是 \"syn-\" 和 \"drome\" 两部分，\"syn-\" 来源于古希腊语，意为 \"合并\"，\"drome\" 来自古希腊，意为 \"奔跑\"，它整体表示的是一系列的症状。\n\n  \n\n### 词缀分析\n\n  \n\n*   AIDS是一个缩写词，由四个不同的词组成，所以并没有词缀。\n\n  \n\n### 发展历史和文化背景\n\n  \n\n*   AIDS 在1981年当时被镶嵌出来，这被公认为历史上第一个被诊断出来的艾滋病病例。这个词首次被美国食品和药物管理局（FDA）和美国疾病控制和预防中心（CDC）提出并广泛接受。\n\n  \n\n### 单词变形\n\n  \n\n*   AIDS 作为疾病的名字，是一个命名词，，没有变型。但是，请注意这个单词在口语中常常全部使用大写（AIDS）。\n\n  \n\n### 记忆辅助\n\n  \n\n*   由于AIDS是由四个英文单词的首字母组成的缩写，所以记忆AIDS，最好是记住这四个单词：Acquired, Immune, Deficiency, Syndrome，然后再将这四个单词的含义串连起来。\n\n  \n\n### 小故事\n\n  \n\nIn a small town, everyone knew Tom had AIDS. Despite the disease, Tom never lost his optimism and continued to help others, becoming an inspiration to those around him. 生活在小镇上的每个人都知道Tom得了艾滋病。尽管有了这个疾病，Tom从未丧失乐观的态度，他继续帮助他人，成为周围人的灵感来源。",
      "reporter_nick_name": "nick_name3",
      "solver_nick_name": null,
      "report_time": "2024-12-13T21:20:15",
      "resolved_time": null,
      "status": "未解决"
    },]);

const selectedMistake = ref(null);

const toggleDetails = (row) => {
    if (selectedMistake.value === row) {
        selectedMistake.value = null; // 隐藏详细内容
    } else {
        selectedMistake.value = row; // 显示选中的详细内容
    }
};

const handleSearch = async () => {
    const params = {
        page: pageNumber.value,
        page_size: pageSize.value,
        status: 0
    };
    // Call the searchMistakeList function to get the data
    const res = await searchMistakeList(params);
    if (res.data.code == '1') {
        totalNumber.value = res.data.data.total; // Update total number
        mistakeData.value = res.data.data.mistakes; // Update mistake data
    } else {
        console.error("获取出错记录失败", res.message);
    }
};

onMounted(() => {
    handleSearch();
});

handleSearch();


const handleExportData = async ()=>{
    //TODO 导出数据库数据

}
</script>