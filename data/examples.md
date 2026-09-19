# 数据集样例与字段说明

本页帮助你在下载数据前理解文件结构。除特别标注外，下面的内容是**字段格式示例**，不是完整数据集。正式实验请以官方下载文件为准。

## 1. MovieLens 100K

MovieLens 100K 的评分文件 `u.data` 是制表符分隔的文本，没有表头：

```text
196    242    3    881250949
186    302    3    891717742
22     377    1    878887116
244    51     2    880606923
166    346    1    886397596
```

字段顺序：

| 字段 | 含义 |
|---|---|
| user_id | 用户编号 |
| item_id | 电影编号 |
| rating | 评分，1–5 |
| timestamp | Unix 时间戳 |

电影信息在 `u.item` 中，常见字段包括电影编号、电影名称、上映日期、IMDb 链接和类型标签。

适合练习：UserCF、ItemCF、矩阵分解、评分预测和 Top-N 推荐。

## 2. Amazon Reviews

Amazon 评论数据通常是一行一个 JSON 对象。官方示例的字段结构如下：

```json
{
  "reviewerID": "A2SUAM1J3GNN3B",
  "asin": "0000013714",
  "reviewerName": "J. McDonald",
  "helpful": [2, 3],
  "reviewText": "Great purchase though!",
  "overall": 5.0,
  "summary": "Heavenly Highway Hymns",
  "unixReviewTime": 1252800000,
  "reviewTime": "09 13, 2009"
}
```

重点字段：

- `reviewerID`：用户 ID
- `asin`：商品 ID
- `overall`：评分
- `reviewText`：评论正文
- `summary`：评论标题
- `unixReviewTime`：交互时间

商品元数据还可能包含商品标题、价格、品牌、类别、图片和“also bought”等关联商品。

适合练习：商品推荐、隐式反馈、文本增强推荐、冷启动和商品关联图。

## 3. Yelp Open Dataset

Yelp 数据主要以 JSON Lines 形式组织。下面是一个**简化的字段结构示意**：

```json
{
  "user_id": "user_001",
  "business_id": "business_101",
  "stars": 5,
  "date": "2024-01-15",
  "text": "The food was excellent.",
  "useful": 2,
  "cool": 1,
  "funny": 0
}
```

评论数据常见字段：

- `user_id)：用户 ID
- `business_id)：商户 ID
- `stars`：评分
- `date`：评论日期
- `text`：评论内容

商户数据还包含名称、类别、城市、经纬度、营业状态和属性等信息。

适合练习：餐馆推荐、地理位置推荐、评论文本分析、长尾和多样性分析。

注意：上面的 JSON 仅用于解释字段结构；下载和使用请遵守 Yelp 官方数据条款。

## 4. MIND 新闻推荐数据集

MIND 主要包含 `behaviors.tsv` 和 `news.tsv`。

### 用户行为示例

```text
1    U001    11/15/2019 8:00 AM    N123 N456    N789-1 N321-0 N654-0
2    U002    11/15/2019 8:05 AM    N222        N111-0 N333-1 N555-0
```

字段顺序：

| 字段 | 含义 |
|---|---|
| impression_id | 曝光记录编号 |
| user_id | 用户编号 |
| time | 曝光时间 |
| history | 用户此前点击过的新闻 ID 序列 |
| impressions | 本次曝光的新闻及点击标签 |

在 `impressions` 中，`N789-1` 表示点击，`N321-0` 表示未点击。

### 新闻内容示例

```text
N123    news    technology    New AI model improves search    A new model was released...    https://example.com/news/123
```

新闻字段通常包括：

- 新闻 ID
- 大类和子类
- 标题
- 摘要
- URL
- 标题实体和摘要实体

适合练习：序列推荐、点击率预测、用户兴趣建模、新闻内容编码和负采样。

## 5. 如何查看真实样例

下载 MovieLens 100K 后，可以执行：

```bash
head -5 data/raw/ml-100k/u.data
head -5 data/raw/ml-100k/u.item
```

查看 JSON Lines 文件时，可以执行：

```bash
head -3 reviews.json
```

如果文件经过 gzip 压缩：

```bash
zcat reviews.json.gz | head -3
```

不要把完整数据集提交到 GitHub。仓库只保存下载说明、处理脚本和必要的小型示例。

