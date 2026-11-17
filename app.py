import google.generativeai as genai
import streamlit as st

# הגדרת עמוד ואופטימיזציה למובייל
st.set_page_config(
    page_title="Social Media Drip Campaigner", page_icon="⚡", layout="centered"
)

# טעינת מפתח ה-API מתוך ה-Secrets של סטרימלייט
if "GEMINI_API_KEY" in st.secrets:
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
  st.error("חסר מפתח GEMINI_API_KEY בהגדרות ה-Secrets בסטרימלייט!")

st.title("⚡ Social Media Drip Campaigner")
st.write("מחולל תוכן שיווקי אוטומטי לרשתות חברתיות מחומר גלם אחד.")

# תיבת קלט לחומר הגלם של המשתמש
raw_input = st.text_area(
    "הכנס כאן חומר גלם, רעיון, או טקסט גולמי:",
    placeholder=(
        "לדוגמה: פתחנו עסק חדש לפתרונות הצללה וציוד שטח מתקדם, המוצר עמיד"
        " במיוחד וקל להתקנה..."
    ),
    height=150,
)

if st.button("🚀 צור קמפיין שיווקי", type="primary"):
  if not raw_input.strip():
    st.warning("נא להזין טקסט או רעיון לפני יצירת הקמפיין.")
  else:
    with st.spinner("מייצר קמפיין שיווקי מותאם אישית לכל הרשתות..."):
      try:
        # שימוש במודל המעודכן
        model = genai.GenerativeModel("gemini-3.8-flash")

        prompt = f"""
                אתה מומחה שיווק דיגיטלי ואסטרטג תוכן.
                בהינתן חומר הגלם הבא, צור עבורי קמפיין שיווקי מלא המחולק ל-3 פלטפורמות שונות:
                
                1. 💼 **LinkedIn Post:** פוסט מקצועי, עסקי, שמוכר ערך ומתאים לנטוורקינג ולקוחות B2B.
                2. 👥 **Facebook Post:** פוסט שיווקי מושך, בגובה העיניים, שמעודד מעורבות ותגובות.
                3. 📸 **Instagram / TikTok Concept:** תסריט קצר/קפשן לרילס/טיקטוק, כולל הצעה לקונספט ויזואלי והאשטאגים חמים (#).
                
                חומר הגלם של המשתמש:
                {raw_input}
                
                הצג את התוצאות בצורה נקייה, מעוצבת ומוכנה להעתקה לכל רשת חברתית.
                """

        response = model.generate_content(prompt)

        st.success("הקמפיין הופק בהצלחה!")
        st.markdown("---")
        st.markdown(response.text)

      except Exception as e:
        st.error(f"אירעה שגיאה בתקשורת עם מנוע ה-AI: {e}")
