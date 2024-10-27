import cohere
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import numpy as np
from sklearn.cluster import KMeans
from flask import Flask, render_template, request


app = Flask(__name__)

# Function to create and display a radar chart of subject grades
def create_subject_radar_chart(subject_grades):
    subjects = list(subject_grades.keys())
    grades = list(subject_grades.values())
   
    angles = np.linspace(0, 2*np.pi, len(subjects), endpoint=False)
    grades = np.concatenate((grades, [grades[0]]))
    angles = np.concatenate((angles, [angles[0]]))
   
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, grades)
    ax.fill(angles, grades, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(subjects)
    ax.set_ylim(0, 100)
    ax.set_title("Subject Performance")
   
    # Save the figure to a file
    plt.savefig('static/subject_performance.png')  # Save radar chart as a static image
    plt.close()  # Close the figure to avoid display

co = cohere.Client('IXCprKXZqVVJtKyb62QnjVVd2gA65OzM4njLMNW0')

def analyze_student(info):
    feedback = f"<h2>Personalized Education Plan for {info['name']}</h2><br>"
   
    # Overall performance
    feedback += "<title>Overall Performance</title><p>"
    if info['grade'] >= 90:
        feedback += "You're excelling! Keep challenging yourself by exploring advanced topics and seeking out opportunities to mentor others. Stay consistent with your effort."
    elif info['grade'] >= 80:
        feedback += "Good performance overall! You have a solid understanding, but try to push yourself a bit further in areas you find difficult. Consider setting specific, measurable goals."
    elif info['grade'] >= 70:
        feedback += "You're doing okay, but there is room for growth. Identify the subjects or skills that need the most attention and work steadily on improving them. Break tasks down into manageable steps."
    else:
        feedback += "Your performance needs improvement, but don't worry — you have the potential to turn things around! Focus on building a strong foundation and seek extra help if needed."
    feedback += "</p>"


    # Attention span
    feedback += "<title>Attention Span</title><p>"
    
    if info['attention_span'] <= 4:
        message1 = "Give a short message about someone who has a low attention span(1-4 on a scale of 1-10) and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean. Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice. headings are h1 and are the subjects.  headings are h1 and are the subjects, and titles. Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long. ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message1,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    elif 5 <= info['attention_span'] <= 7:
        message2 = "Give a short message about someone who has a medium attention span(5-7 on a scale of 1-10) and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3.Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message2,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    else:
        message3 = "Give a short message about someone who has a high attention span(8-10 on a scale of 1-10) and how they could maintain it and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3 . Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message3,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    feedback += "</p>"


    # Behavior
    feedback += "<title>Behavior</title><p>"
    if info['behavior'] <= 3:
        message4 = "Give a short message about someone who has a behavior in class(range from 1-3 on a scale of 1-10) and how they could improve their behavior to excel. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice. headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3 . Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message4,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    elif 5 <= info['attention_span'] <= 7:
        message5 = "Give a short message about someone who has a medium behavior in class(range from 5-7 on a scale of 1-10) and how they could improve their behavior to excel. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3 . Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message5,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    else:
        message6 = "Give a short message about someone who has a high behavior in class(8-10 on a scale of 1-10)and how they could maintain it their behavior excel. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3 . Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message6,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    feedback += "</p>"


    # Willingness to Learn
    feedback += "<title>Willingness to Learn</title><p>"
    if info['willingness'] <= 4:
        message7 = "Give a short message about someone who has a low willingness to learn(1-4 on a scale of 1-10) and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.subheadings are the little dividers like the conclusion and stuff. make it h3 . Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message7,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    elif 5 <= info['attention_span'] <= 7:
        message8 = "Give a short message about someone who has a medium willingness to learn(5-7 on a scale of 1-10) and how they could improve better. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message8,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    else:
        message9 = "Give a short message about someone who has a high willingness to learn(8-10 on a scale of 1-10) and how they could maintain it and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
        response = co.chat(
        message=message9,
        model="command",
        temperature=0.3
        )
        feedback += response.text
    feedback += "</p>"


    # Subject-specific recommendations
    feedback += "<title>Subject-Specific Recommendations</title><br>"
    for subject, grade in info['subject_grades'].items():
        feedback += f"<title>{subject}</title><p>"
        if 90 <= grade <= 100:
            message10 = f"Give a short message about someone who has a great grade in {subject}(Grade of 90-100) and how they could maintain it and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
            response = co.chat(
            message=message10,
            model="command",
            temperature=0.3
        )   
            feedback += response.text
            
        elif 80 <= grade <= 89:
            message11 = f"Give a short message about someone who has a good grade in {subject}(Grade of 80-89) and how they could improve. Make it user friendly to read instead of a chunky paragraph, and have bullet points and bolded words. Inside the message, give a straightforward message so I can copy and paste it to the student, do give me text inside saying things like(say this to your student) or (is this text good?). Provide a professional message without developer suggestions or additional notes. DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app. Use <b> and then put what you want to say and then end with </b> for bold. use html for any special properties.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
            response = co.chat(
            message=message11,
            model="command",
            temperature=0.3
            )
            feedback += response.text
        elif 70 <= grade <= 79:
          message12 = f"Give a short message about someone who has a decent grade in {subject}(Grade of 70-79) and how they could improve.Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
          response = co.chat(
          message=message12,
          model="command",
          temperature=0.3
          )
          feedback += response.text
        elif 60 <= grade <=69:
          message13 = f"Give a short message about someone who has a barely passing grade in {subject}(Grade of 60-69) and how they could improve. Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
          response = co.chat(
          message=message13,
          model="command",
          temperature=0.3
          )
          feedback += response.text
        else:
          message14 = f"Give a short message about someone who has a failing grade in {subject}(Grade of <=59) and how they could improve.Make it user friendly and DO NOT GIVE ANY DEVELOPER NOTES, this goes straight to the person through an app, dont mention anything in 1st person. Use <b> tag and then put what you want to say and then end with </b> for bold. use html for any special properties. Break up the text, and for each and every different part of the plan, use the format of a couple sentences about the grade, bullet points about what you could do, subheadings for different parts of the plan, and list information with bullet points below that and then a couple of sentences for a conclusion of the grade and further thoughts. Again, NO DEVELOPER NOTES and NO 1st PERSON!! dont ahve any weird variables like [app name] in the text. The text should be readable like a formal presentation. make the text clean.Format the response in HTML using bullet points (<ul> and <li>) for suggestions and use <strong> tags for key advice.headings are h1 and are the subjects.Subheadings are the little dividers like the conclusion and stuff. make it h3. Add links to the text for extra info for practice, and dont make the subheadings or titles too long.ADD LINKS!! THE SUBHEADINGS THAT RE NOT THE TITLES SHOULD BE SMALLER THAN THE TITLE AND SHORT.<br>"
          response = co.chat(
          message=message14,
          model="command",
          temperature=0.3
          )
          feedback += response.text
        feedback += "</p>"
    
    return feedback



# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')


# Route to generate the education plan
@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    # Your logic to generate the plan and plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    # Your plotting code here...
    info = {
        'name': request.form['name'],
        'grade': float(request.form['grade']),
        'attention_span': int(request.form['attention_span']),
        'behavior': int(request.form['behavior']),
        'willingness': int(request.form['willingness']),
        'iq': int(request.form['iq']),
        'subject_grades': {
            'Math': float(request.form['math_grade']),
            'Science': float(request.form['science_grade']),
            'English': float(request.form['english_grade']),
            'History': float(request.form['history_grade']),
            'Computer Science': float(request.form['Computer_Science_grade'])
        }
    }


    create_subject_radar_chart(info['subject_grades'])  # Create the radar chart
    feedback = analyze_student(info)  # Analyze student info and get feedback
    return render_template('plan.html', plan=feedback)


if __name__ == '__main__':
    app.run(debug=True)