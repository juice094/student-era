# 实验一：基于 ERDAS 9.2 的遥感图像处理

## 实验目的

通过 ERDAS 9.2 软件读取图像及信息查询，对图像进行色彩变换获取关键信息，完成图像融合与卷积增强处理。

## 实验环境

- Windows 系统
- ERDAS IMAGINE 9.2 软件

## 实验数据

| 文件 | 大小 | 说明 |
|------|------|------|
| `data/erdas92/water.img` | ~100KB | 水体遥感影像 |
| `data/erdas92/1.img` | ~470KB | 高分辨率参考影像 |

## 实验步骤

### 1. 图像读取及信息查看

1. 主界面中点击 **Viewer**，新建 Viewer 界面
2. 在 Viewer1 中选择 **File → Open → Raster Layer**
   - File 选项卡中选择 `water.img`
   - Raster Option 选项卡中，Display as 选择 **True Color**
   - 勾选 **Fit to Frame**，点击 OK
3. 新建 Viewer2，选择 `statellite3.img`
   - Raster Option 选项卡中 Display as 选择 **Gray Scale**
   - 勾选 **Fit to Frame**，点击 OK

### 2. 色彩变换（RGB → IHS）

1. 主界面 → **Interpreter → Spectral Enhancement → RGB to IHS**
2. Input File 中选择 `water.img`
3. Output File 中输入 `waternew.img`
4. 点击 OK
5. 新建 Viewer1 读取 `waternew.img`，查看色彩变换后的图片

### 3. 基于分辨率的图像融合

1. 主界面 → **Interpreter → Spatial Enhancement → Resolution Merge**
2. 参数设置：
   | 参数 | 值 |
   |------|-----|
   | High Resolution Input File | `1.img` |
   | Multispectral Input File | `water.img` |
   | Output File | `merge.tiff` |
   | Method | Principal Component |
   | Resampling Techniques | Cubic Convolution |
   | Output Image Options | Ignore Zero Stats |
3. 点击 OK
4. 新建 Viewer 读取 `merge.tiff`，查看融合图

### 4. 卷积增强处理

1. 主界面 → **Interpreter → Spatial Enhancement → Convolution**
2. 参数设置：
   | 参数 | 值 |
   |------|-----|
   | Input File | `water1.img` |
   | Kernel | 3x3 High Pass |
   | Output File | `enhance.img` |
   | Data Type | Unsigned 8bit |
   | Handle Edges By | Reflection |
3. 点击 OK
4. 新建 Viewer 读取 `enhance.img`，查看增强图

## 实验报告要求

1. 截图对比原始图像与色彩变换后图像
2. 截图展示分辨率融合结果
3. 截图展示卷积增强效果
4. 分析各处理步骤对图像的影响

## 参考资源

- [ERDAS IMAGINE 官方文档](https://www.hexagongeospatial.com/products/erdas-imagine)
- [遥感图像处理基础教程](https://www.bilibili.com/video/BV1q54y1G7j5)
