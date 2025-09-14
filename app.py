from flask import Flask, render_template, abort

app = Flask(__name__)

faculty_data = {
    'dean': {
        'name': 'Dr. Menchie A. Dela Cruz',
        'title': 'Dean of CCIT',
        'image': '/static/images/faculty/dean.png',
        'bio': 'Oversees the College of Communication and Information Technology with academic and administrative leadership.'
    },
    'cs_chair': {
        'name': 'Carl Angelo S. Pamplona, MSCS',
        'title': 'Computer Science Program Chair',
        'image': '/static/images/faculty/pamplona.png',
        'bio': 'Guides the Computer Science program with expertise in software development and computing education.'
    },
    'it_chair': {
        'name': 'Geoffrey S. Sepillo, Ed.D.',
        'title': 'Information Technology Program Chair',
        'image': '/static/images/faculty/sepillo.png',
        'bio': 'Leads the Information Technology program with a focus on educational innovation and applied IT practices.'
    },
    'cs_faculty': [
        {'name': 'Hansel S. Ada, MSCS', 'specialization': 'Computer Science', 'image': '/static/images/faculty/ada.png'},
        {'name': 'John Lenon E. Agatep, Ph.D.', 'specialization': 'Computer Science', 'image': '/static/images/faculty/agatep.png'},
        {'name': 'Daniel A. Bachillar, MSCS', 'specialization': 'Computer Science', 'image': '/static/images/faculty/bachillar.png'},
        {'name': 'Israel M. Cabasug, MSCS', 'specialization': 'Computer Science', 'image': '/static/images/faculty/cabasug.png'},
        {'name': 'Nemia M Galang, Ph.D.', 'specialization': 'Computer Science', 'image': '/static/images/faculty/galang.png'},
        {'name': 'Joseph J. Juliano, MSCS', 'specialization': 'Computer Science', 'image': '/static/images/faculty/juliano.png'},
        {'name': 'Marionne Joyce F. Tapado, MSCS', 'specialization': 'Computer Science', 'image': '/static/images/faculty/tapado.jpg'}
    ],
    'it_faculty': [
        {'name': 'Jason S. Artates, MIT', 'specialization': 'Information Technology', 'image': '/static/images/faculty/artates.png'},
        {'name': 'Fiel M. Dullas Jr., MIT', 'specialization': 'Information Technology', 'image': '/static/images/faculty/dullas.png'},
        {'name': 'Rowela Gongora, MIT', 'specialization': 'Information Technology', 'image': '/static/images/faculty/gongora.png'},
        {'name': 'Melojean C. Marave, Ph.D.', 'specialization': 'Information Technology', 'image': '/static/images/faculty/marave.png'},
        {'name': 'Darwin M. Moraña, MIT', 'specialization': 'Information Technology', 'image': '/static/images/faculty/darwin.png'},
        {'name': 'Daryl John Ragadio, MIT.', 'specialization': 'Information Technology', 'image': '/static/images/faculty/ragadio.png'}
    ]
}

organizations_data = [
    {
        'name': 'College of Communication and Information Technology - Student Body Organization',
        'image': '/static/images/ccitsbo.jpg',
        'description': 'The College of Communication and Information Technology (CCIT) Student Body Organization (SBO) at President Ramon Magsaysay State University (PRMSU) in Iba is the official student government for all CCIT students. The CCIT-SBO is led by a set of elected student officers and is responsible for representing the interests and addressing the concerns of its constituents.',
        'link': '/organizations/ccitsbo',
        'page':'https://www.facebook.com/prmsumain.ccit.sbo'
    },
    {
        'name': 'Association of Students for Communication and Information Interchange',
        'image': '/static/images/ascii.jpg',
        'description': 'The ASCII is a group specifically for students taking up a Bachelor of Science in Computer Science (BSCS) at PRMSU.',
        'link': '/organizations/ascii',
        'page':'https://www.facebook.com/prmsumain.ccit.ascii'
    },
    {
        'name': 'Development, Innovation, and Growth for Information Technology Students (DIGITS)',
        'image': '/static/images/digits.jpg',
        'description': 'The DIGITS is a group specifically for students taking up a Bachelor of Science in Information Technology (BSIT) at PRMSU.',
        'link': '/organizations/digits',
        'page':'https://www.facebook.com/prmsu.ccit.digits'
    }
]

news_data = [
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


gallery_data = {
    'building': [
        {'image': '/static/images/gallery/building1.jpg', 'title': 'CCIT Main Building', 'description': 'Modern architecture with state-of-the-art facilities'},
        {'image': '/static/images/gallery/building2.jpg', 'title': 'Innovation Center', 'description': 'Hub for research and development'},
        {'image': '/static/images/gallery/building3.jpg', 'title': 'Computer Labs', 'description': 'Advanced computing facilities'},
        {'image': '/static/images/gallery/building4.jpg', 'title': 'Library & Study Areas', 'description': 'Quiet spaces for learning and research'}
    ],
    'events': [
        {'image': '/static/images/gallery/event1.jpg', 'title': 'Tech Symposium 2024', 'description': 'Annual technology conference'},
        {'image': '/static/images/gallery/event2.jpg', 'title': 'Hackathon Winners', 'description': 'Students showcasing innovative solutions'},
        {'image': '/static/images/gallery/event3.jpg', 'title': 'Career Fair', 'description': 'Connecting students with industry leaders'},
        {'image': '/static/images/gallery/event4.jpg', 'title': 'Research Showcase', 'description': 'Faculty and student research presentations'}
    ],
    'students': [
        {'image': '/static/images/gallery/student1.jpg', 'title': 'Collaborative Learning', 'description': 'Students working together on projects'},
        {'image': '/static/images/gallery/student2.jpg', 'title': 'Lab Sessions', 'description': 'Hands-on programming experience'},
        {'image': '/static/images/gallery/student3.jpg', 'title': 'Graduation Day', 'description': 'Celebrating academic achievements'},
        {'image': '/static/images/gallery/student4.jpg', 'title': 'Study Groups', 'description': 'Peer-to-peer learning sessions'}
    ]
}

slideshow_images = [
    {'image': '/static/images/slideshow/slideshow1.jpg', 'title': 'Welcome to CCIT', 'subtitle': 'Where Innovation Meets Education'},
    {'image': '/static/images/slideshow/slideshow2.jpg', 'title': "CCIT Celebrates Women's Month", 'subtitle': ''},
    {'image': '/static/images/slideshow/slideshow3.jpg', 'title': 'CCIT New Building', 'subtitle': 'Learn from Industry Leaders'},
    {'image': '/static/images/slideshow/slideshow4.jpg', 'title': 'Bright Future Ahead', 'subtitle': 'Your Success is Our Mission'}
]

@app.route('/')
def home():
    return render_template('index.html', title='Home - CCIT', slideshow=slideshow_images)

@app.route('/about')
def about():
    return render_template('about.html', title='About - CCIT')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html', title='Faculty - CCIT', faculty=faculty_data)

@app.route('/organizations')
def organizations():
    return render_template('organizations.html', title='Student Organizations - CCIT', organizations=organizations_data)

@app.route('/organizations/<org_name>')
def organization_detail(org_name):
    # Find organization by name or return 404
    org = next((org for org in organizations_data if org['link'].split('/')[-1] == org_name), None)
    if not org:
        abort(404)
    return render_template('organization_detail.html', title=f"{org['name']} - CCIT", organization=org)

@app.route('/news')
def news():
    return render_template('news.html', title='News - CCIT', news=news_data)

@app.route('/departments')
def departments():
    return render_template('departments.html', title='Departments - CCIT')

@app.route('/departments/computer-science')
def cs_department():
    return render_template('cs_department.html', title='Computer Science - CCIT')

@app.route('/departments/information-technology')
def it_department():
    return render_template('it_department.html', title='Information Technology - CCIT')

@app.route('/terms')
def terms():
    return render_template('terms.html', title='Terms and Conditions - CCIT')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title='Privacy Policy - CCIT')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='404 - Page Not Found'), 404

if __name__ == '__main__':
    app.run(debug=True)
