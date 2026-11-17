from google import genai
import streamlit as st

# הגדרת עמוד ואופטימיזציה למובייל
st.set_page_config(
    page_title="Social Media Drip Campaigner", page_icon="⚡", layout="centered"
)

# טעינת מפתח ה-API מתוך ה-Secrets של סטרימלייט בצורה בטוחה
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.error("חסר מפתח GEMINI_API_KEY בהגדרות ה-Secrets בסטרימלייט!")
  client = None
else:
  client = genai.Client(api_key=api_key)

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
  elif not client:
    st.error("לא ניתן להתחבר ל-AI עקב היעדר מפתח API.")
  else:
    with st.spinner("מייצר קמפיין שיווקי מותאם אישית לכל הרשתות..."):
      try:
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

        # שימוש בשם המודל המדויק שהמערכת דרשה בהודעת השגיאה
        response = client.models.generate_content(
            model="models/gemini-3.8-flash", contents=prompt
        )

        st.success("הקמפיין הופק בהצלחה!")
        st.markdown("---")
        st.markdown(response.text)

      except Exception as e:
        st.error(f"אירעה שגיאה בתקשורת עם מנוע ה-AI: {e}")
