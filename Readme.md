Pariksha Mukti: University Exam Papers Portal

A platform where students can download previous year exam papers of different universities, contribute to the site, interact with each other to collaborate on projects and academics, and buy and sell notes.

Table of Contents:

1. Features
2. Technologies Used
3. Installation
4. Usage
5. Contributing
6. License
7. Contact

Features:

1. Download Exam Papers: Access previous year exam papers from various universities.
2. Contribute Content: Upload and share exam papers and notes.
3. Collaborate: Interact with other students to collaborate on projects and academic activities.
4. Marketplace: Buy and sell study notes.

Technologies Used:

1. Backend: Flask
2. Frontend: HTML, CSS
3. Database: MySQL
4. APIs: RESTful APIs with Flask

Installation
To get a local copy up and running, follow these steps:

1. Clone the repository:
git clone https://github.com/pankajsharma1022/Pariksha_Mukti.git
cd Pariksha_Mukti

2. Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt

4. Set up the database:
flask db init
flask db migrate
flask db upgrade

5. Run the application
flask run

Usage:
After setting up the project, you can access it in your web browser at http://127.0.0.1:5000.

Example usage:
. Download Papers: Navigate to the "Download Papers" section and select your university and course.
. Upload Content: Go to the "Contribute" section to upload exam papers or notes.
. Interact with Students: Use the "Collaborate" section to join discussion forums.
. Marketplace: Visit the "Marketplace" to buy or sell study materials.

Contributing:

We welcome contributions to improve the platform! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

Please ensure your code adheres to our coding guidelines and includes appropriate tests.

License:

This project is licensed under the MIT License - see the LICENSE file for details.

Contact:

If you have any questions or suggestions, feel free to contact me:

Email: pankysharma1022@gmail.com
GitHub: https://github.com/pankajsharma1022