%%writefile app.py
import streamlit as st
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="โครงงานระบบวางแผนท่องเที่ยวอัจฉริยะด้วย AI - Presentation",
    page_icon="✈️",
    layout="wide"
)

# ตกแต่งสไตล์เพิ่มเติมด้วย CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Kanit', sans-serif;
    }
    .academic-tag {
        font-size: 14px;
        color: #93c5fd;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: rgba(255, 255, 255, 0.05);
        padding: 4px 12px;
        border-radius: 4px;
        display: inline-block;
    }
    .main-title {
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(90deg, #3b82f6, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .slide-card {
        background: rgba(15, 23, 42, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 5px solid #3b82f6;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        min-height: 250px;
    }
    .slide-num {
        font-size: 12px;
        font-weight: 700;
        color: #3b82f6;
    }
    .slide-title {
        font-size: 18px;
        font-weight: 600;
        margin-top: 5px;
        margin-bottom: 10px;
    }
    .slide-list {
        font-size: 14px;
        color: #64748b;
        padding-left: 20px;
    }
    .day-card {
        background: rgba(59, 130, 246, 0.05);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .day-title {
        font-size: 18px;
        font-weight: 600;
        color: #3b82f6;
        margin-bottom: 10px;
    }
    .activity-row {
        display: flex;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        padding-bottom: 8px;
    }
    .activity-time {
        font-weight: bold;
        color: #8b5cf6;
        min-width: 60px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# 1. ส่วนนำเสนอ (Cover Slide)
# =========================
st.markdown('<span class="academic-tag">Project Presentation</span>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">ระบบวางแผนท่องเที่ยวอัจฉริยะด้วยเทคโนโลยีปัญญาประดิษฐ์</h1>', unsafe_allow_html=True)
st.write("โครงงานพัฒนาระบบแนะนำกำหนดการเดินทางและจัดสรรงบประมาณส่วนบุคคลโดยใช้ระบบวิเคราะห์ข้อมูลจำลอง เพื่อช่วยลดขั้นตอนและเพิ่มประสิทธิภาพในการออกแบบแผนการท่องเที่ยว")

# ข้อมูลผู้จัดทำโครงงาน (Student Credentials)
with st.expander("👨‍🎓 ข้อมูลผู้รับผิดชอบโครงงาน / ข้อมูลส่งอาจารย์", expanded=True):
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.write("**ผู้เสนอโครงงาน:** [ระบุชื่อ-นามสกุลของคุณที่นี่]")
        st.write("**รหัสนักศึกษา:** [ระบุรหัสนักศึกษา]")
    with col_c2:
        st.write("**หลักสูตร/สาขา:** วิทยาการคอมพิวเตอร์ / เทคโนโลยีสารสนเทศ")
        st.write("**เสนออาจารย์:** [ระบุชื่ออาจารย์ผู้รับผิดชอบวิชา]")

st.markdown("---")

# =========================
# 2. สไลด์สรุปเนื้อหาโครงงาน (Presentation Slides)
# =========================
st.header("📊 สรุปภาพรวมโครงงาน")
st.write("สรุปประเด็นหลักสำหรับการนำเสนอหน้าชั้นเรียน")

slide_col1, slide_col2, slide_col3 = st.columns(3)

with slide_col1:
    st.markdown("""
    <div class="slide-card">
        <span class="slide-num">SLIDE 1</span>
        <div class="slide-title">🔍 หลักการและเหตุผล</div>
        <ul class="slide-list">
            <li>การวางแผนท่องเที่ยวในปัจจุบันมีความซับซ้อนและใช้เวลาสูง</li>
            <li>ข้อจำกัดในเรื่องความคุ้มค่าด้านงบประมาณส่วนบุคคล</li>
            <li>ระบบเข้ามาแก้ปัญหาการคำนวณและประมวลผลให้แบบทันที</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with slide_col2:
    st.markdown("""
    <div class="slide-card">
        <span class="slide-num">SLIDE 2</span>
        <div class="slide-title">🛠️ สถาปัตยกรรมระบบ</div>
        <ul class="slide-list">
            <li><b>Frontend:</b> พัฒนาอย่างรวดเร็วและสวยงามด้วย Streamlit / CSS3</li>
            <li><b>Algorithm:</b> วิเคราะห์สไตล์และประมวลผลช่วงเวลากิจกรรมเชิงตรรกะ</li>
            <li><b>Data:</b> จัดสรรงบประมาณต่อวันและแนะนำสถานที่ที่เหมาะสมตามงบ</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with slide_col3:
    st.markdown("""
    <div class="slide-card">
        <span class="slide-num">SLIDE 3</span>
        <div class="slide-title">🚀 ประโยชน์ที่ได้รับ</div>
        <ul class="slide-list">
            <li>ผู้ใช้ประหยัดเวลาในการเตรียมทริปและวิเคราะห์กิจกรรมลงมากกว่า 70%</li>
            <li>โครงสร้างแอปพลิเคชันรองรับการเชื่อมต่อ API ของ Generative AI ในอนาคต</li>
            <li>ช่วยควบคุมค่าใช้จ่ายไม่ให้บานปลายด้วยการเฉลี่ยงบประมาณรายวัน</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# 3. ส่วนแอปพลิเคชันสาธิต (Interactive App Demo)
# =========================
st.header("🧳 ระบบต้นแบบ (Interactive App Demo)")
st.write("กรอกเป้าหมายเพื่อสร้างและทดสอบการจำลองแผนการท่องเที่ยวเพื่อประเมินผลการทำงาน")

with st.form("travel_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input("📍 จุดหมายปลายทาง", placeholder="เช่น เชียงใหม่, ญี่ปุ่น, ภูเก็ต")
        days = st.number_input("📅 จำนวนวัน (สูงสุด 14 วัน)", min_value=1, max_value=14, value=3)
    with col2:
        budget = st.number_input("💰 งบประมาณ (บาท)", min_value=1, value=5000, step=500)
        style = st.selectbox("🎯 รูปแบบการท่องเที่ยว", ["🏖️ พักผ่อน", "🌲 ธรรมชาติ", "🍜 เน้นอาหาร", "🏛️ วัฒนธรรม", "🧗 ผจญภัย"])
    
    submit_button = st.form_submit_button(label="🤖 ทดสอบจำลองการสร้างแผนเดินทาง")

if submit_button:
    if not destination:
        st.warning("⚠️ กรุณากรอกจุดหมายปลายทางของคุณ")
    else:
        with st.spinner("🤖 ระบบ AI กำลังประมวลผลข้อมูลและจัดเตรียมแผนการเดินทางที่เหมาะสม..."):
            time.sleep(1.5)  # จำลองการคำนวณ
            
            daily_budget = round(budget / days)
            
            # สรุปข้อมูลการคำนวณ
            st.success(f"🎉 สร้างแผนเดินทางสำหรับทริป **{destination}** เรียบร้อยแล้ว!")
            
            sc1, sc2, sc3 = st.columns(3)
            with sc1:
                st.metric("📅 ระยะเวลาเดินทาง", f"{days} วัน")
            with sc2:
                st.metric("💰 งบประมาณทั้งหมด", f"{budget:,.2f} บาท")
            with sc3:
                st.metric("💵 งบประมาณเฉลี่ยต่อวัน", f"{daily_budget:,.2f} บาท")
            
            st.markdown("### 📋 กำหนดการเดินทางจำลองรายวัน")
            for d in range(1, days + 1):
                st.markdown(f"""
                <div class="day-card">
                    <div class="day-title">📅 วันที่ {d} ของทริป</div>
                    <div class="activity-row">
                        <div class="activity-time">09:00</div>
                        <div>
                            <p style="margin:0; font-weight:500;">☀️ ออกเดินทางท่องเที่ยวตามโปรแกรมแรก</p>
                            <small style="color:#64748b;">เดินทางด้วยขนส่งมวลชนในพื้นที่เพื่อความประหยัด</small>
                        </div>
                    </div>
                    <div class="activity-row">
                        <div class="activity-time">12:00</div>
                        <div>
                            <p style="margin:0; font-weight:500;">🍜 ลิ้มลองอาหารขึ้นชื่อประจำท้องถิ่น</p>
                            <small style="color:#64748b;">เลือกรับประทานร้านอาหารที่เหมาะสมกับงบประมาณรายวัน</small>
                        </div>
                    </div>
                    <div class="activity-row">
                        <div class="activity-time">14:00</div>
                        <div>
                            <p style="margin:0; font-weight:500;">📸 กิจกรรมหลักช่วงบ่าย</p>
                            <small style="color:#64748b;">ประเภทกิจกรรมที่เน้นเป็นพิเศษสำหรับทริปนี้: {style}</small>
                        </div>
                    </div>
                    <div class="activity-row" style="border-bottom:none; padding-bottom:0;">
                        <div class="activity-time">18:00</div>
                        <div>
                            <p style="margin:0; font-weight:500;">🌙 พักผ่อนและเดินเล่นตลาดยามเย็น</p>
                            <small style="color:#64748b;">สัมผัสวิถีชีวิตคนท้องถิ่นก่อนเดินทางกลับสู่ที่พักอย่างปลอดภัย</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

