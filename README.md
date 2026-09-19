# 推荐系统课程项目

面向人工智能学院大三学生的推荐系统课程项目模板。学生需要基于公开数据集完成一个可复现的推荐方案，并提交代码、实验报告和结果分析。

## 项目目标

- 理解从数据处理、候选生成、排序到评测的完整推荐流程
- 掌握协同过滤、矩阵分解、隐式反馈和内容增强推荐等方法
- 养成时间切分、负采样、离线评测、消融实验和可复现提交习惯

## 数据集路线

| 难度 | 数据集 | 典型任务 |
|---|---|---|
| 入门 | MovieLens 100K | 评分预测、UserCF、ItemCF、MF、Top-N |
| 进阶 | MovieLens 1M / 20M | BPR、NCF、冷启动、侧信息 |
| 开放选题 | Amazon Reviews、Yelp | 商品/商户推荐、文本增强、地理推荐 |
| 挑战 | MIND | 新闻推荐、序列建模、点击率预测 |

数据集不会直接存入本仓库。请先阅读 `data/README.md`，使用下载脚本获得数据，并遵守各数据集的许可条款。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python scripts/download_movielens.py --size 100k
python scripts/prepare_movielens.py --input data/raw/ml-100k --output data/processed/movielens-100k
```

## 统一实验要求

1. 默认按时间切分训练集、验证集和测试集；不得随机打乱后切分。
2. 只使用训练集构造用户历史和候选集，避免数据泄漏。
3. 至少报告 Recall@K、NDCG@K、HitRate@K；评分预测任务另报 RMSE/MAE。
4. 至少包含一个简单 baseline，并说明改进来自哪里。
5. 固定随机种子，记录数据集版本、运行环境和主要超参数。

## 提交内容

请复制 `submission-template/`，将目录命名为 `submissions/<学号>-<姓名或队名>/`，提交：

- `README.md`：问题定义、方法、运行方式和结论
- `src/`：核心代码
- `configs/`：配置文件
- `reports/`：实验结果、图表和误差分析
- `requirements.txt`：依赖版本

详见 `docs/assignment.md` 和 `docs/evaluation.md`。

第一次使用 GitHub 的同学请先阅读 `docs/github-guide.md`，按指南完成 Fork、Clone、分支、Push 和 Pull Request。

## 许可说明

本仓库中的课程文字、脚本和模板采用 MIT License。外部数据集仍以其原始提供方的许可和使用条款为准；本仓库不重新分发原始数据。
