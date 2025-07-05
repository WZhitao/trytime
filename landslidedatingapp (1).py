# app.py
import ee
import geemap.foliumap as geemap
import streamlit as st

# ———— 1. Earth Engine 初始化 ————
# 首次运行时按需替换成你的认证方式：
# ee.Initialize()

# ———— 2. Streamlit 页面标题 ————
st.title("底图切换示例")

# ———— 3. 创建地图对象 ————
m = geemap.Map(
    center=[61.5, 100],
    zoom=18,
    add_google_map=True,      # 打开 Google 地图支持
    plugin_Draw=False,
    locate_control=False
)
# 默认就已经加载了 Google 卫星底图
m.add_basemap("SATELLITE")

# ———— 4. 侧边栏按钮 ————
# 只有在 streamlit run 模式下，这个按钮才会出现在网页左侧
if st.sidebar.button("加载铁路图层"):
    m.add_basemap("OpenRailwayMap")
    st.sidebar.success("已添加铁路图层")

# ———— 5. 渲染地图 ————
st.subheader("地图视图")
m.to_streamlit(height=500)
