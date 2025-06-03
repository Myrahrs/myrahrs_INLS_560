# ----------------------------------------------
# MODULE IMPORTS
# ----------------------------------------------
import os  # Built-in module for interacting with the operating system (e.g., file creation)
import re  # Built-in module for regular expressions, used to manipulate strings

# ----------------------------------------------
# FUNCTION: slugify
# PURPOSE: Convert a page title to a URL-friendly filename (slug)
# ----------------------------------------------

def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Special case: If the title is 'Home', use 'index.html'
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"  # Replace non-word chars with hyphens and add .html

# ----------------------------------------------
# FUNCTION: generate_nav
# PURPOSE: Create navigation bar HTML with active page highlighted
# ----------------------------------------------
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""  # Start with empty string for nav links
    for title in titles:  # Loop through each title in the list
        filename = slugify(title)  # Convert title to slug/filename
        active_class = ' class="active"' if title == active_title else ""  # Add class if this is the current page
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'  # Add link to nav bar
    return nav_links.strip()  # Remove trailing newline

# ----------------------------------------------
# FUNCTION: create_html_file
# PURPOSE: Generate and save an HTML file for a given page title
# ----------------------------------------------
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)  # Convert title to slug
    nav = generate_nav(titles, active_title=title)  # Get navigation bar HTML

    # Custom content for each page
    page_content = {
        "Home": "<p>Welcome to my educational consulting page. I support learners, educators, and institutions with personalized strategies for success.</p>",

        "About Me": """
            <h2>Dr. Myrah Stockdale (Ph.D. ABD)</h2>
            <h3>Education</h3>
            <ul>
                <li>Ph.D. Candidate (ABD) in Educational Research</li>
                <li>M.Ed. in Curriculum and Instruction</li>
            </ul>
            <h3>Experience</h3>
            <ul>
                <li>10+ years in higher education leadership</li>
                <li>Led multiple accreditation processes across health disciplines</li>
            </ul>
            <h3>Publications</h3>
            <ul>
                <li>Chapter: Accreditation in Veterinary Education (2024)</li>
                <li>Several peer-reviewed articles on program evaluation</li>
            </ul>
        """,

        "Services": """
            <h2>Consulting Services</h2>
            <p>I offer personalized consulting services in the following areas:</p>
            <ul>
                <li>Accreditation Preparation</li>
                <li>Assessment Strategy</li>
                <li>Curriculum Design</li>
                <li>Faculty Development</li>
            </ul>
            <h3>Rates</h3>
            <p><strong>Hourly:</strong> $150/hr<br>
            <strong>Project-based:</strong> Contact for a custom quote.</p>
        """,

        "Testimonials": """
            <h2>What Clients Say</h2>
            <blockquote>
                \"Ms. Stockdale's support during our accreditation process was invaluable. Her attention to detail and encouragement kept our team on track.\"
                <footer>– Program Director, Public Health</footer>
            </blockquote>
            <blockquote>
                \"We couldn’t have redesigned our curriculum without her guidance!\"
                <footer>– Dean, School of Pharmacy</footer>
            </blockquote>
        """,

        "Resources": """
            <h2>Free Resources</h2>
            <ul>
                <li><a href=\"#\">Accreditation Self-Study Checklist</a></li>
                <li><a href=\"#\">Assessment Planning Template</a></li>
                <li><a href=\"#\">Faculty Workshop Toolkit</a></li>
            </ul>
        """,

        "My Experience": "<p>Coming soon: Detailed timeline of professional experience and leadership impact.</p>",
        "My Projects": "<p>Coming soon: Portfolio of consulting and educational innovation projects.</p>"
    }

    # HTML content using f-string for dynamic content
    html_content = f"""
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>{title}</title>
        <link rel=\"stylesheet\" href=\"style.css\">
    </head>
    <body>
        <nav>
            {nav}  <!-- Navigation bar inserted here -->
        </nav>
        <div class=\"content\">
            <h1>{title}</h1>  <!-- Main heading of the page -->
            {page_content.get(title, "<p>Content coming soon.</p>")}
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)  # Create full output path
    os.makedirs(output_dir, exist_ok=True)  # Make sure output directory exists

    with open(output_path, 'w') as file:  # Open file in write mode
        file.write(html_content)  # Write the HTML content

    print(f"Created {filename} in the '{output_dir}' directory.")  # Notify user

# ----------------------------------------------
# FUNCTION: create_css_file
# PURPOSE: Generate and save a basic CSS file for styling the pages
# ----------------------------------------------
def create_css_file(output_dir="build"):
    """Generate and write the style.css file based on a dictionary of styles."""
    styles = {
        "font-family": "Calibri",  # Base font for the website
        "body-background": "#7BAFD4",  # Background color for the body
        "nav-background": "#13294B",  # Navigation bar background color
        "nav-a-color": "#4B9CD3",  # Link color in nav
        "nav-a-active-color": "#ffffff"  # Link color for the active page
    }

    # CSS file content using f-string for style values
    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """

    css_path = os.path.join(output_dir, "style.css")  # Set path for CSS file
    with open(css_path, 'w') as file:  # Open file in write mode
        file.write(css_content)  # Write CSS content to file

    print(f"Created style.css in the '{output_dir}' directory.")  # Notify user

# ----------------------------------------------
# MAIN FUNCTION
# PURPOSE: Orchestrates page and style generation
# ----------------------------------------------
def main():
    titles = ["Home", "About Me", "My Experience", "My Projects", "Services", "Testimonials", "Resources"]

    for title in titles:
        create_html_file(title, titles)  # Uses default output_dir="build"

    create_css_file()  # Uses default output_dir="build"

# ----------------------------------------------
# ENTRY POINT
# ----------------------------------------------
if __name__ == "__main__":
    main()  # Run the main function
