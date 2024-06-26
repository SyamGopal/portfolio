import streamlit as st

# Function to display contact information
def display_contact():
    st.subheader("Contact")
    st.write("""
    - **Email:** syamgopalmeda@gmail.com
    - **Phone:** 9502524924
    - **LinkedIn:** [linkedin.com/in/syam-gopal-meda-9b3967232](https://www.linkedin.com/in/syam-gopal-meda-9b3967232)
    - **GitHub:** [SyamGopal (github.com)](https://github.com/SyamGopal)
    - **Address:** D.no:30/980, Chinna Ullingipalem, Machilipatnam, Andhra Pradesh, 521001
    """)

    st.subheader("Contact Form")
    full_name = st.text_input("Full Name", key="full_name")
    email_address = st.text_input("Email Address", key="email_address")
    message = st.text_area("Your Message", key="message")

    if st.button("Send Message"):
        st.success("Message sent successfully!")

# Main function
def main():
    # CSS styles with additional background colors
    css = """
    /* Header */
h1 {
    color: #2c3e50;
    background-color: #f7dc6f;
    padding: 15px;
    border-radius: 5px;
    animation: fadeInDown 1s ease-out;
}

/* Subheader */
h2 {
    color: #2980b9;
    background-color: #ff7675;
    padding: 10px;
    border-radius: 5px;
    animation: fadeInDown 1s ease-out;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: #fdcb6e;
    animation: slideInLeft 1s ease-out;
}

/* Navigation Radio Button */
.sidebar .radio-item label {
    color: #34495e;
    background-color: #6c5ce7;
    padding: 5px 10px;
    border-radius: 5px;
    animation: fadeInLeft 1s ease-out;
}

/* Contact Form */
.stTextInput>div>div>div>input,
.stTextArea>div>div>textarea {
    background-color: #00b894;
    border-color: #bdc3c7;
    animation: fadeIn 1s ease-out;
}

.stButton>button {
    background-color: #fd79a8 !important;
    animation: fadeIn 1s ease-out;
}

/* Footer */
footer {
    color: #7f8c8d;
    background-color: #0984e3;
    padding: 10px;
    border-radius: 5px;
    animation: fadeInUp 1s ease-out;
}

/* Animation Keyframes */
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        transform: translateX(-100%);
    }
    to {
        transform: translateX(0);
    }
}

    """

    # Load custom CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    # Header section
    st.title("Meda Syam Gopal's Portfolio")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Meda Syam Gopal")
    st.sidebar.image("profile photo.png", use_column_width=True)

    # Navigation
    nav_selection = st.sidebar.radio("Go to",
                                     ["About", "Skills", "Projects", "Education", "Work Experience", "Certifications", "Contact"])

    # Page content
    if nav_selection == "About":
        # About Section
        st.header("About Me")
        st.write("""
        I am Meda Syam Gopal, a passionate and dedicated individual with a keen interest in computer science and technology. I am currently pursuing a B.Tech in Computer Science and Engineering at RVR & JC College of Engineering. I have a strong foundation in programming languages such as C, Java, HTML, and Python. I am highly motivated to learn and grow in the field of technology.
        """)
        st.subheader("Strengths")
        st.write("""
        - Communication
        - Problem-solving
        - Teamwork
        - Learning
        - Analytical thinking
        - Logical reasoning
        """)
        st.subheader("Areas of Interests")
        st.write("Networking, Web development, Mobile development")
        st.subheader("Hobbies")
        st.write("Playing shuttle, writing programming, browsing the internet")

    elif nav_selection == "Skills":
        # Skills Section
        st.header("Skills")
        st.subheader("Programming Languages")
        st.write("- C\n- Java\n- HTML\n- Python")
        st.subheader("Databases")
        st.write("- SQL")
        st.subheader("Data Analysis")
        st.write("- Data organization and analysis\n- Data visualization using Python libraries\n- Creating reports and presentations with relevant data")
        st.subheader("Other Skills")
        st.write("- Proficiency in Excel for data entry and management\n- Strong teamwork skills\n- Effective oral communication")

    elif nav_selection == "Projects":
        # Projects Section
        st.header("Projects")
        st.subheader("Mango Leaves Disease Detection")
        st.write("""
        - **Role:** Developer
        - **Team Size:** 2
        - **Project Duration:** 1 Month
        - **Technologies Used:** Python, TensorFlow, OpenCV
        - **Description:** Developed a machine learning model to detect diseases in mango leaves. The project involved:
            - Collecting and preprocessing a dataset of healthy and diseased mango leaves.
            - Using image processing techniques with OpenCV to enhance the images.
            - Building a Convolutional Neural Network (CNN) using TensorFlow to classify the leaves as healthy or diseased.
            - Achieving a high accuracy rate in detecting different types of leaf diseases.
            - Deploying the model using a simple web interface for ease of use by farmers and agricultural experts.
        """)

        st.subheader("Cyber Security in Website Scraper Project")
        st.write("""
        - **Role:** Developer
        - **Team Size:** 3
        - **Project Duration:** 2 Months
        - **Technologies Used:** Python, Flask, SQL, Machine Learning
        - **Description:** Developed a secure web scraping application with enhanced cybersecurity measures. The project involved:
            - Implementing authentication mechanisms to ensure only authorized users could access the scraper.
            - Using encryption techniques to secure data transmission and storage.
            - Incorporating access controls to restrict user permissions based on roles.
            - Developing anomaly detection algorithms using machine learning to identify and prevent malicious activities.
            - Creating a user-friendly dashboard with Flask to monitor scraping activities and detected anomalies.
            - Ensuring compliance with legal and ethical standards in web scraping practices.
        """)

    elif nav_selection == "Education":
        # Education Section
        st.header("Education")
        st.write("""
        - **B.Tech in Computer Science and Engineering:** RVR & JC College of Engineering, Aacharya Nagarjuna University, 7.6 CGPA (Pursuing)
        - **Diploma in Computer Management Engineering:** A.A.N.M & V.V.R.S.R Polytechnic College, State Board of Technical Education and Training, 83.67%, 2021
        - **SSC:** Nirmala High School, Board of Secondary Education, Andhra Pradesh, 85%, 2018
        """)

    elif nav_selection == "Work Experience":
        # Work Experience Section
        st.header("Work Experience")
        st.subheader("Intern")
        st.write("""
        - **Company:** ABC Technologies
        - **Duration:** June 2022 - August 2022
        - **Role:** Software Development Intern
        - **Responsibilities:**
            - Assisted in developing and maintaining web applications.
            - Collaborated with the development team to implement new features.
         - Participated in code reviews and provided feedback.
         - Tested and debugged applications to ensure optimal performance.
         """)
    elif nav_selection == "Certifications":
        # Certifications Section
        st.header("Certifications")
        st.subheader("Python for Data Science")
        st.write("""
                - **Institution:** Coursera
                - **Year:** 2023
                """)

        st.subheader("Web Development Bootcamp")
        st.write("""
                - **Institution:** Udemy
                - **Year:** 2022
                """)

    elif nav_selection == "Contact":
        display_contact()

    # Footer
    st.markdown("---")
    st.write("© 2024 Meda Syam Gopal. All rights reserved")

if __name__ == "__main__":
    main()
