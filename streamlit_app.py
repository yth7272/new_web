from prototype_runtime import render_template, setup_page


setup_page("Main Page", require_auth=True)
render_template("templates/01_main_page.html")
