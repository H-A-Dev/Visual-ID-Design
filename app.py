import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="هوية سياحة المملكة", layout="wide")

# عنوان مبدئي
st.title("لوحة تحكم الهوية البصرية - لون الخزامى")
st.write("أهلاً بكِ! هنا سنعرض أكواد الهوية التي صممناها.")

# زر لاختبار الألوان
color = st.color_picker("جربي درجة لون الخزامى", "#967BB6")
st.write(f"الدرجة الحالية هي: {color}")

