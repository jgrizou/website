---
style: Navbar
brand:
  name: Jonathan Grizou
  link: {{ "/" | web_path}}
navbar:
  - name: home
    link: {{ "/" | web_path}}
    display: Home

  - name: projects
    link: {{ "/projects" | web_path}}
    display: Projects

  - name: publications
    link: {{ "/publications" | web_path}}
    display: Publications

  - dropdown:
      display: More
      item:
        - link: {{ "/blog/open_science" | web_path}}
          display: Open Science
        - link: {{ "/blog/p_values" | web_path}}
          display: P-Values
        - link: {{ "/misc" | web_path}}
          display: Misc
        - link: {{ "/cv" | web_path}}
          display: CV

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
