# LMS Components/Component, Stock and Assembly Management System

This system is meant to help small teams organize their electronic components. 
Create components and assemblies, print bill of materials, import or export excel files
and manage your stock. You may also use the internal time tracking mechanism to keep
track on what your time was spent on.

> **Bold** items are currently implemented

## Components Management

- **Create, edit, import or export packages. Packages may have alternative names.**
- **Create, edit, import or export components that use formerly defined packages.**
- **Create, edit**, import or export categories to better manage components.
- Add ordering information to components
- Search for components
- Check what systems/assemblies a component is used in

## Assembly Management
- Create or import assemblies. These are collections of components that specify
- which and how many components are used to build a system.
- Search for and view assemblies
- Import/Export bill of materials
- Export a list of components that are needed for a given number of systems to be built.
- If used with the Stock Manager, the list will contain the number of components available
and the number of components that are missing

## Stock Management

Keep track of your stock: 
- How many components are available and where are they stored?
- Move components, combine batches of components or split components into multiple batches

## Time Tracking

- Track your time at work
- Create projects and tasks
- Start and stop time logging on a specified task with a few clicks
- Get an overview of time spent on different tasks for a specific project
   
# Status

> Currently broken due to not using fixed versions for dependencies, see #1

> This project was an effort based on me not being happy with how components
> were "managed" in the company I worked at at the time. The companies boss
> expected the employees to use components in new projects that have
> previously been used whenever possible (as they were already tested and
> most likely to be found somewhere in our storage boxes). However, there was
> no easy way to find out what components have been used in numerous projects
> over the last years, as we just had a
> bunch of bill of material excel tables, burried in network folders for each
> project.
> 
> I tried to address the issue multiple times, until I started this project. On
> presenting the state this software is currently in, the reaction was "no not
> another tool!" and they started manually merging all excel tables to one huge
> master table.
> 
> I lost the motivation to continue this project and will probably not pick it
> up again, as I would rather use Elixir/Phoenix and a Graph Database nowadays.

# Setup

- create a virtual environment and activate it
``` bash
virtualenv venv
source ./venv/bin/activate
```
- install dependencies
``` bash
pip install -r requirements.txt
```

- setup a MySQL database. Add your URL and credentials in `settings.py`

- setup the database tables using
``` BASH
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

- start the server
``` BASH
python manage.py runserver
```

