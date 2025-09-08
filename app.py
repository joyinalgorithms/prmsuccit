from flask import Flask, render_template, request
import os

app = Flask(__name__)

# SEO and meta data
def get_meta_data(page_title, description=""):
    return {
        'title': f"{page_title} - CCIT | College of Communication and Information Technology",
        'description': description or "College of Communication and Information Technology - Leading education in Computer Science and Information Technology",
        'keywords': "CCIT, Computer Science, Information Technology, College, University, Education, Technology"
    }

@app.route('/')
def home():
    meta = get_meta_data("Home", "Welcome to the College of Communication and Information Technology - Shaping the future of technology education")
    return render_template('home.html', meta=meta)

@app.route('/about')
def about():
    meta = get_meta_data("About Us", "Learn about our vision, mission, goals and quality policy at CCIT")
    return render_template('about.html', meta=meta)

@app.route('/faculty')
def faculty():
    meta = get_meta_data("Faculty", "Meet our distinguished faculty members from Computer Science and Information Technology departments")

    faculty_data = {
        'dean': {
            'name': 'Dr. Menchie A. Dela Cruz',
            'position': 'Dean of CCIT',
            'image': '/static/images/faculty/dean.png',
            'department': 'Administration'
        },
        'cs_chair': {
            'name': 'Carl Angelo S. Pamplona, MSCS',
            'position': 'Computer Science Program Chair',
            'image': '/static/images/faculty/pamplona.png',
            'department': 'Computer Science'
        },
        'it_chair': {
            'name': 'Geoffrey S. Sepillo, Ed.D.',
            'position': 'Information Technology Program Chair',
            'image': '/static/images/faculty/sepillo.png',
            'department': 'Information Technology'
        },
        'cs_faculty': [
            {'name': 'Hansel S. Ada, MSCS', 'image': '/static/images/faculty/ada.png'},
            {'name': 'John Lenon E. Agatep, Ph.D.', 'image': '/static/images/faculty/agatep.png'},
            {'name': 'Daniel A. Bachillar, MSCS', 'image': '/static/images/faculty/bachillar.png'},
            {'name': 'Israel M. Cabasug, MSCS', 'image': '/static/images/faculty/cabasug.png'},
            {'name': 'Nemia M Galang, Ph.D.', 'image': '/static/images/faculty/galang.png'},
            {'name': 'Joseph J. Juliano, MSCS', 'image': '/static/images/faculty/juliano.png'}

        ],
        'it_faculty': [
            {'name': 'Jason S. Artates, MIT', 'image': '/static/images/faculty/artates.png'},
            {'name': 'Fiel M. Dullas Jr., MIT', 'image': '/static/images/faculty/dullas.png'},
            {'name': 'Rowela Gongora, MIT', 'image': '/static/images/faculty/gongora.png'},
            {'name': 'Melojean C. Marave, Ph.D.', 'image': '/static/images/faculty/marave.png'},
            {'name': 'Darwin M. Moraña, MIT', 'image': '/static/images/faculty/darwin.png'},
            {'name': 'Daryl John Ragadio, MIT.', 'image': '/static/images/faculty/ragadio.png'}

        ]
    }

    return render_template('faculty.html', meta=meta, faculty=faculty_data)

@app.route('/organizations')
def organizations():
    meta = get_meta_data("Student Organizations", "Discover student organizations and their leadership in CCIT")

    organizations = [
        {
            'name': 'College of Communication and Information Technology - Student Body Organization',
            'description': 'Advancing computer science education and innovation',
            'officers': [
                {'name': 'Dave Anthony Ulanday', 'position': 'President'},
                {'name': 'Lovely Joyce Palmarin', 'position': 'Vice President-Internal'},
                {'name': 'Rhonielyn Tolentino', 'position': 'Vice President-External'},
                {'name': 'Eunice Aceron', 'position': 'Secretary'},
                {'name': 'Bea Cybelle Siccion', 'position': 'Assistant Secretary'},
                {'name': 'Allaine Candelario', 'position': 'Treasurer'},
                {'name': 'Luofin Andrei Sombillo', 'position': 'Assistant Treasurer'},
                {'name': 'Selah Faith Ferrer', 'position': 'Auditor'},
                {'name': 'Daniela Villanueva', 'position': 'Assistant Auditor'},
                {'name': 'Daniele Quiesha Diaz', 'position': 'Public Information Officer'},
                {'name': 'Engelbert Bautista', 'position': 'Sergeant at Arms'},
                {'name': 'Donald Ryan Dumangas', 'position': 'Sergeant at Arms'},
                {'name': 'Michael Justin Alegado', 'position': 'Sergeant at Arms'},
                {'name': 'Felix Ordillas II', 'position': 'Sergeant at Arms'},
                {'name': 'Reymar James Espirida', 'position': 'Business Manager'},
                {'name': 'John Ronald Mendoza', 'position': 'Business Manager'},
                {'name': 'Kim Danielle Feria', 'position': 'Business Manager'},
                {'name': 'Jackie Mae Febrero', 'position': 'Business Manager'},
                {'name': 'Mary Gwynneth Mercurio', 'position': 'Muse'},
                {'name': 'Georg Mikhael Tan', 'position': 'Escort'},
                {'name': 'Shaina Gunas', 'position': '1st year Representative'},
                {'name': 'Rinalyne Giron', 'position': '2nd year Representative'},
                {'name': 'Mark Airon Padao', 'position': '3rd year Representative'},
                {'name': 'Christine Joy Bernal', 'position': '4th year Representative'},
            ],
            'platform': 'Promoting coding competitions, hackathons, and tech workshops'
        },

        {
            'name': 'Association of Students for Communication and Information Interchange (ASCII)',
            'description': 'Connecting CS students with industry professionals',
            'officers': [
                {'name': 'Alyssa Paradeza', 'position': 'President'},
                {'name': 'Chyna Alexis Bacolod', 'position': 'Vice President-Internal'},
                {'name': 'Krizia Mae Funiestas', 'position': 'Secretary'},
                {'name': 'Angelica Aquino', 'position': 'Treasurer'},
                {'name': 'Julie Cansino', 'position': 'Auditor'},
                {'name': 'Bermel Ken Achacoso', 'position': 'Public Information Officer'},
                {'name': 'Christine Joy Bernal', 'position': 'Sergeant at Arms'},
                {'name': 'James Ryan Alferos', 'position': 'Sergeant at Arms'},
                {'name': 'Daisy Ann Magno', 'position': 'Business Manager'},
                {'name': 'Nahci Garcia', 'position': 'Business Manager'},
                {'name': 'Sharmaine Baluyot', 'position': 'Muse'},
                {'name': 'Ronnie Dolueras Jr.', 'position': 'Escort'},
                {'name': 'Marbert Tabile', 'position': '1st year Representative'},
                {'name': 'Dean Jeu Day', 'position': '2nd year Representative'},
                {'name': 'Louis Philip Falaminiano', 'position': '3rd year Representative'},
                {'name': 'Daniele Quiesha Diaz', 'position': '4th year Representative'},
            ],
            'platform': 'Industry networking, certification programs, and career development'
        },
        {
            'name': 'Development, Innovation and Growth for Information Technology Students (DIGITS)',
            'description': 'Fostering innovation and entrepreneurship in technology',
            'officers': [
                 {'name': 'Janna Fiel de Guzman', 'position': 'President'},
                {'name': 'Mean Dianne Lego', 'position': 'Vice President-Internal'},
                {'name': 'Veronica Joy Pavia', 'position': 'Vice President-External'},
                {'name': 'Charley Padua', 'position': 'Secretary'},
                {'name': 'Martha Nicole Exala', 'position': 'Treasurer'},
                {'name': 'Jherzel Artates', 'position': 'Auditor'},
                {'name': 'Norhanna Bakal', 'position': 'Public Information Officer'},
                {'name': 'John Rey Dar', 'position': 'Sergeant at Arms'},
                {'name': 'Lynus Philip Aguado', 'position': 'Sergeant at Arms'},
                {'name': 'Abegaille Asuncion', 'position': 'Business Manager'},
                {'name': 'Kim Lance Eyano', 'position': 'Business Manager'},
                {'name': 'Princess Joana Lee', 'position': 'Muse'},
                {'name': 'Georg Mikhael Tan', 'position': 'Escort'},
                {'name': 'Jillian Mhaie dela Cruz', 'position': '1st year Representative'},
                {'name': 'Rina Mae Dimaano', 'position': '2nd year Representative'},
                {'name': 'Jerselle Mulato', 'position': '3rd year Representative'},
                {'name': 'Charlene Abuen', 'position': '4th year Representative'},
            ],
            'platform': 'Startup incubation, innovation challenges, and tech entrepreneurship'
        }
    ]

    return render_template('organizations.html', meta=meta, organizations=organizations)

@app.route('/news')
def news():
    meta = get_meta_data("College News", "Stay updated with the latest news and events from CCIT")

    news_items = [
        {
            'title': '𝟏𝟏𝟖𝐭𝐡 𝐁𝐢𝐫𝐭𝐡 𝐀𝐧𝐧𝐢𝐯𝐞𝐫𝐬𝐚𝐫𝐲 𝐨𝐟 𝐏𝐫𝐞𝐬𝐢𝐝𝐞𝐧𝐭 𝐑𝐚𝐦𝐨𝐧 𝐌𝐚𝐠𝐬𝐚𝐲𝐬𝐚𝐲',
            'date': '2025-08-31',
            'summary': 'Known as the “𝐂𝐡𝐚𝐦𝐩𝐢𝐨𝐧 𝐨𝐟 𝐭𝐡𝐞 𝐌𝐚𝐬𝐬𝐞𝐬,” President Magsaysay’s legacy of humility, integrity, and dedication to public service continued to inspire generations of Filipinos. His leadership reminded us that true governance is rooted in service to the people..',
            'image': '/static/images/news/news0.jpg'
        },
        {
            'title': '𝐂𝐂𝐈𝐓-𝐒𝐁𝐎 𝐎𝐚𝐭𝐡-𝐓𝐚𝐤𝐢𝐧𝐠 & 𝐂𝐁𝐋 𝐑𝐞𝐯𝐢𝐬𝐢𝐨𝐧 𝟐𝟎𝟐𝟓–𝟐𝟎𝟐𝟔',
            'date': '2025-08-22',
            'summary': 'On August 20, 2025, the newly elected officers of the College of Communication and Information Technology - Student Body Organization (CCIT-SBO) convened for their first official meeting of the academic year.',
            'image': '/static/images/news/news1.jpg'
        },
        {
            'title': '𝐈𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐢𝐧𝐠 𝐭𝐡𝐞 𝐍𝐞𝐰𝐥𝐲 𝐄𝐥𝐞𝐜𝐭𝐞𝐝 𝐂𝐂𝐈𝐓-𝐒𝐁𝐎 𝐎𝐟𝐟𝐢𝐜𝐞𝐫𝐬',
            'date': '2025-08-18',
            'summary': '𝐈𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐢𝐧𝐠 𝐭𝐡𝐞 𝐍𝐞𝐰𝐥𝐲 𝐄𝐥𝐞𝐜𝐭𝐞𝐝 𝐂𝐂𝐈𝐓-𝐒𝐁𝐎 𝐎𝐟𝐟𝐢𝐜𝐞𝐫𝐬 for this academic year 2025-2025.',
            'image': '/static/images/news/news2.jpg'
        },
        {
            'title': 'CCIT Student Body Organization Election',
            'date': '2025-08-08',
            'summary': 'CCIT Student Body Organization conducted the election of officers for this academic year.',
            'image': '/static/images/news/news3.jpg'
        }
    ]

    return render_template('news.html', meta=meta, news=news_items)

@app.route('/computer-science')
def computer_science():
    meta = get_meta_data("Computer Science Department", "Explore our comprehensive Computer Science programs and curriculum")
    return render_template('computer_science.html', meta=meta)

@app.route('/information-technology')
def information_technology():
    meta = get_meta_data("Information Technology Department", "Discover our innovative Information Technology programs and opportunities")
    return render_template('information_technology.html', meta=meta)

@app.route('/terms')
def terms():
    meta = get_meta_data("Terms of Service", "Terms and conditions for using the CCIT website")
    return render_template('terms.html', meta=meta)

@app.route('/privacy')
def privacy():
    meta = get_meta_data("Privacy Policy", "Privacy policy and data protection information for CCIT website users")
    return render_template('privacy.html', meta=meta)

@app.errorhandler(404)
def not_found(error):
    meta = get_meta_data("Page Not Found", "The requested page could not be found")
    return render_template('404.html', meta=meta), 404

if __name__ == '__main__':
    app.run(debug=True)
