---
style: Navbar
brand: Jonathan Grizou
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
      display: Drop
      item:
        - link: {{ "/test" | web_path}}
          display: Test

  - side: right
    name: about
    link: {{ "/about" | web_path}}
    display: About

  - side: right
    name: contact
    link: {{ "/contact" | web_path}}
    display: Contact
---
