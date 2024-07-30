from app import app
from views import main_view
# view/Home Page Render
app.add_url_rule("/", view_func=main_view.HomepageHandler.as_view('home'))

# view/Create Cloud Form Register
app.add_url_rule(
    "/cloud-create", view_func=main_view.CloudCreateHandler.as_view('cloud_create'))

# view/success redirection after form-submission
app.add_url_rule(
    '/success', view_func=main_view.SuccessReDirect.as_view('success'))

# view/search specific cloud details
app.add_url_rule('/', view_func=main_view.SearchView.as_view('search_view'))

# view/total cloud-Registered
app.add_url_rule('/', view_func=main_view.TotalCloud.as_view('total_cloud'))

# view/render base.html
app.add_url_rule('/', view_func=main_view.BaseHtmlView.as_view('base'))

#view;/update-cloud-Details
app.add_url_rule('/update',view_func=main_view.CloudDetailsUpdate.as_view('update_cloud'))

#view/login-logout-Details
app.add_url_rule('/login-logout',view_func=main_view.Authentication.as_view('login/logout_cloud'))

#view/profile
app.add_url_rule('/Profile',view_func=main_view.Profile.as_view('Profile'))

