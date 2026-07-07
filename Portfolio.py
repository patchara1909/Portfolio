from pathlib import Path

portfolio_data = {
    "title": "PORTFOLIO",
    "name": "นางสาว พัชราภรณ์ ขีดขัน",
    "position": "นักศึกษาสาขาวิศวกรรมคอมพิวเตอร์และเทคโนโลยีอุตสาหกรรม",
    "summary": "สนใจด้าน Artificial Intelligence, Internet of Things, Embedded Systems และการพัฒนาซอฟต์แวร์สำหรับแก้ปัญหาและสร้างนวัตกรรม",
    "contact": {
        "email": "auma66404@gmail.com",
        "phone": "096-779-5123",
        "line": "khedkin_0909",
        "address": "มหาวิทยาลัยราชภัฏพิบูลสงคราม"
    },
    "categories": [
        {"title": "ประวัติส่วนตัว", "href": "#about", "description": "ข้อมูลพื้นฐาน ทักษะและความสนใจ"},
        {"title": "ประวัติการศึกษา", "href": "#education", "description": "ระดับการศึกษาและสถานศึกษา"},
        {"title": "ประสบการณ์ฝึกทักษะ", "href": "#skills", "description": "ทักษะด้านซอฟต์และฮาร์ดแวร์"},
        {"title": "กิจกรรมและฝึกอบรม", "href": "#activities", "description": "โครงการอบรม แข่งขัน และกิจกรรม"},
        {"title": "โครงการที่เคยทำ", "href": "#projects", "description": "ผลงานและโปรเจกต์เด่น"},
        {"title": "เกียรติบัตร", "href": "#certificates", "description": "หลักฐานการฝึกอบรมและรางวัล"},
    ],
    "skills": {
        "soft": ["Problem Solving", "Analytical Thinking", "Creativity", "Teamwork", "Communication", "Time Management", "Adaptability"],
        "hard": ["PLC OMRON", "CAD/CAE Tools", "C/C++", "Python", "JavaScript", "MongoDB", "SQL", "Raspberry Pi", "ESP32"],
        "tools": ["SolidWorks 3D", "Embedded Systems", "IoT", "Automation", "Robotics"]
    },
    "education": [
        {"institution": "มหาวิทยาลัยราชภัฏพิบูลสงคราม", "degree": "นักศึกษาวิศวกรรมคอมพิวเตอร์และเทคโนโลยีอุตสาหกรรม", "detail": "กำลังเรียนและพัฒนาทักษะด้าน AI, IoT และระบบอัตโนมัติ"},
        {"institution": "วิทยาลัยเทคโนโลยีอุตสาหกรรม", "degree": "ประกาศนียบัตรวิชาชีพ", "detail": "เน้นทักษะทางเทคโนโลยีและการปฏิบัติ"},
        {"institution": "โรงเรียนมอุตม์", "degree": "มัธยมศึกษาตอนปลาย", "detail": "เกรดเฉลี่ย 3.67"},
    ],
    "activities": [
        "เข้าร่วมโครงการอบรมเชิงปฏิบัติการและแข่งขันทักษะด้านความมั่นคงปลอดภัยทางไซเบอร์ (Cyber Hackathon)",
        "เข้าร่วมโครงการ CyberNet Pro และ AI Agent Coding Camp",
        "อบรมด้าน IoT, Embedded Systems และการพัฒนาทักษะด้าน AI",
        "เข้าร่วมโครงการฝึกอบรมพัฒนาทักษะการใช้ปัญญาประดิษฐ์กับการวิจัย"
    ],
    "projects": [
        {"name": "Safe Smoke", "detail": "เว็บแอปพลิเคชันสำหรับตรวจจับสถานการณ์ควันและแจ้งเตือนความปลอดภัย"},
        {"name": "Smart Car", "detail": "ระบบรถยนต์ไฟฟ้าสำหรับช่วยให้การขับขี่ปลอดภัยและมีประสิทธิภาพ"},
        {"name": "EquaChem", "detail": "แอปพลิเคชันที่เกี่ยวข้องกับการจัดการข้อมูลและการเรียนรู้ด้านเคมี"},
        {"name": "Automatic Attendance System", "detail": "ระบบตรวจสอบการเข้างานด้วยการจดจำใบหน้าและการยืนยันตัวตนแบบ 2FA"}
    ],
    "certificates": [
        "PSRU Cyber Hackathon #2",
        "PSRU Cyber Hackathon #3",
        "R2M Competition",
        "อบรม Python และการพัฒนาแอปพลิเคชัน",
        "อบรม AI และ IoT"
    ],
}


def build_list(items, tag='li'):
    return ''.join(f'<{tag}>{item}</{tag}>' for item in items)


def build_cards(items, kind='text'):
    if kind == 'education':
        return ''.join(
            f'<article class="card"><h4>{item["institution"]}</h4><p><strong>{item["degree"]}</strong></p><p>{item["detail"]}</p></article>'
            for item in items
        )
    if kind == 'projects':
        return ''.join(
            f'<article class="card"><h4>{item["name"]}</h4><p>{item["detail"]}</p></article>'
            for item in items
        )
    return ''.join(f'<article class="card"><p>{item}</p></article>' for item in items)


toc_html = ''.join(
    f'<a class="toc-card" href="{item["href"]}"><h4>{item["title"]}</h4><p>{item["description"]}</p></a>'
    for item in portfolio_data['categories']
)

about_html = f'''
<section id="about" class="section">
  <div class="section-title">
    <p class="eyebrow">ประวัติส่วนตัว</p>
    <h3>ข้อมูลพื้นฐาน</h3>
  </div>
  <div class="card-grid">
    <article class="card">
      <h4>ข้อมูลทั่วไป</h4>
      <ul>
        <li>ชื่อ: {portfolio_data['name']}</li>
        <li>อีเมล: {portfolio_data['contact']['email']}</li>
        <li>โทรศัพท์: {portfolio_data['contact']['phone']}</li>
        <li>LINE ID: {portfolio_data['contact']['line']}</li>
      </ul>
    </article>
    <article class="card">
      <h4>จุดมุ่งหมาย</h4>
      <p>พัฒนาทักษะด้าน AI, IoT และการพัฒนาซอฟต์แวร์เพื่อสร้างนวัตกรรมที่มีประโยชน์ต่อสังคมและอุตสาหกรรม</p>
    </article>
  </div>
</section>
'''

education_html = f'''
<section id="education" class="section">
  <div class="section-title">
    <p class="eyebrow">ประวัติการศึกษา</p>
    <h3>สถานศึกษาและระดับการเรียน</h3>
  </div>
  <div class="card-list">{build_cards(portfolio_data['education'], 'education')}</div>
</section>
'''

skills_html = f'''
<section id="skills" class="section">
  <div class="section-title">
    <p class="eyebrow">ประสบการณ์ฝึกทักษะ</p>
    <h3>ทักษะและความสามารถ</h3>
  </div>
  <div class="card-grid">
    <article class="card">
      <h4>Soft Skills</h4>
      <ul>{build_list(portfolio_data['skills']['soft'])}</ul>
    </article>
    <article class="card">
      <h4>Hard Skills</h4>
      <ul>{build_list(portfolio_data['skills']['hard'])}</ul>
    </article>
    <article class="card">
      <h4>Tools & Platforms</h4>
      <ul>{build_list(portfolio_data['skills']['tools'])}</ul>
    </article>
  </div>
</section>
'''

activities_html = f'''
<section id="activities" class="section">
  <div class="section-title">
    <p class="eyebrow">กิจกรรมและฝึกอบรม</p>
    <h3>ประสบการณ์ด้านกิจกรรม</h3>
  </div>
  <div class="card-list">{build_cards(portfolio_data['activities'])}</div>
</section>
'''

projects_html = f'''
<section id="projects" class="section">
  <div class="section-title">
    <p class="eyebrow">โครงการที่เคยทำ</p>
    <h3>ผลงานเด่น</h3>
  </div>
  <div class="card-list">{build_cards(portfolio_data['projects'], 'projects')}</div>
</section>
'''

certificates_html = f'''
<section id="certificates" class="section">
  <div class="section-title">
    <p class="eyebrow">เกียรติบัตร</p>
    <h3>ใบรับรองและรางวัล</h3>
  </div>
  <div class="card-list">{build_cards(portfolio_data['certificates'])}</div>
</section>
'''

html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{portfolio_data['title']}</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="hero">
    <div class="hero-content">
      <p class="eyebrow">PORTFOLIO</p>
      <h1>{portfolio_data['name']}</h1>
      <h2>{portfolio_data['position']}</h2>
      <p>{portfolio_data['summary']}</p>
      <a href="#toc" class="btn">ดูสารบัญ</a>
    </div>
  </header>

  <main>
    <section id="toc" class="section">
      <div class="section-title">
        <p class="eyebrow">สารบัญ</p>
        <h3>เมนูตามหมวดหมู่</h3>
      </div>
      <div class="toc-grid">{toc_html}</div>
    </section>
    {about_html}
    {education_html}
    {skills_html}
    {activities_html}
    {projects_html}
    {certificates_html}
  </main>

  <footer>
    <p>สร้างขึ้นจากไฟล์พอร์ตโฟลิโอ PDF โดยอัตโนมัติ</p>
  </footer>
</body>
</html>
'''

styles = """* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, sans-serif;
  color: #1f2937;
  background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 100%);
  line-height: 1.6;
}
a { text-decoration: none; color: inherit; }
.hero {
  padding: 90px 24px 70px;
  background: linear-gradient(120deg, #0f4c81 0%, #2563eb 100%);
  color: white;
}
.hero-content { max-width: 900px; margin: 0 auto; }
.eyebrow { letter-spacing: 0.25em; text-transform: uppercase; font-size: 0.8rem; opacity: 0.8; margin-bottom: 8px; }
.hero h1 { font-size: 2.2rem; margin: 0 0 8px; }
.hero h2 { font-size: 1.1rem; margin: 0 0 12px; font-weight: 500; }
.btn {
  display: inline-block; margin-top: 16px; padding: 10px 18px; border-radius: 999px; background: white; color: #0f4c81; font-weight: 700;
}
.section { max-width: 1100px; margin: 0 auto; padding: 48px 24px; }
.section-title { margin-bottom: 20px; }
.section-title h3 { margin: 0; font-size: 1.4rem; }
.toc-grid, .card-grid { display: grid; gap: 16px; }
.toc-grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.card-grid { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.card-list { display: grid; gap: 16px; }
.toc-card, .card {
  background: white; border-radius: 16px; padding: 20px; box-shadow: 0 10px 30px rgba(15, 76, 129, 0.08); border: 1px solid #e5e7eb;
}
.toc-card:hover { transform: translateY(-2px); transition: 0.2s; }
.toc-card h4, .card h4 { margin-top: 0; margin-bottom: 8px; }
ul { margin: 0; padding-left: 18px; }
footer { text-align: center; padding: 24px; color: #6b7280; }
@media (max-width: 700px) { .hero { padding-top: 70px; } .hero h1 { font-size: 1.7rem; } }
"""

base = Path(__file__).resolve().parent
(base / "index.html").write_text(html, encoding="utf-8")
(base / "styles.css").write_text(styles, encoding="utf-8")
print("Generated index.html and styles.css")
