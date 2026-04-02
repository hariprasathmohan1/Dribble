# Case Study: Dribble Clone
## Date:02.04.2026

## AIM:
To create a simplified clone of Dribbble (https://dribbble.com/) landing page.


## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Design a navigation bar with links: Inspiration, Find Work, Learn Design, Go Pro, Sign In, Sign Up.

### Step 5:
Add a catchy headline with a search bar.

### Step 6:
Use ```<div>``` containers for each dribbble shot thumbnail.

### Step 7:
Include designer name and likes count below each image.

### Step 8:
Include text like “Find your next design inspiration” with a button (“Join Dribbble” or “Explore”).

### Step 9:
Create a footer with your name and register number.

### Step 10:
Publish the website in the LocalHost.

## PROGRAM :
```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Simple Dribble Clone</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand fw-bold" href="#">Dribbble</a>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-3">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Shots</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Designers</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Teams</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Community</a>
                    </li>
                </ul>

                <form class="d-flex me-3">
                    <input class="form-control" type="search" placeholder="Search">
                </form>

                <button class="btn btn-outline-light me-2">Sign in</button>
                <button class="btn btn-danger">Sign up</button>
            </div>
        </div>
    </nav>

    <div class="container-fluid bg-light py-5">
        <div class="container text-center">
            <h2 class="fw-bold">What are you working on?</h2>
            <p class="text-muted">Dribble is a place for designers to share their work.</p>
            <button class="btn btn-secondary me-2">Learn More</button>
            <button class="btn btn-danger">Sign Up</button>
        </div>
    </div>

    <div class="container my-4">
        <div class="row">
            <div class="col text-center">
                <h3>Popular Shots</h3>
                <p class="text-muted">Simple design inspirations</p>
            </div>
        </div>
    </div>

    <div class="container mb-4">
        <div class="row g-2">

            <div class="col-md-2 col-sm-2">
                <div class="card">
                    <img src=".avif" class="card-img-top" alt="design1">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 1</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-2 col-sm-2">
                <div class="card">
                    <img src="colours.jpg" class="card-img-top" alt="design2">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 2</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-3 col-sm-3">
                <div class="card">
                    <img src="bolt.jpg" class="card-img-top" alt="design3">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 3</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-1 col-sm-1">
                <div class="card">
                    <img src="usain.jpg" class="card-img-top" alt="design4">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 4</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-1 col-sm-1">
                <div class="card">
                    <img src="download (2).avif" class="card-img-top" alt="design5">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 5</h5>
                        
                    </div>
                </div>
            </div>

            <div class="col-md-3 col-sm-3">
                <div class="card">
                    <img src="s.avif" class="card-img-top" alt="design6">
                    <div class="card-body">
                        <h5 class="card-title">Dribble 6</h5>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <footer class="bg-dark text-white text-center py-3">
        <p class="mb-0">M.Hari prasath - (25018172)</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```


## OUTPUT:
![alt text](<harib/alwaysapp/static/Screenshot (45).png>)


## RESULT:
The project for responsive web design in creating a clone of dribble.com is completed successfully.

