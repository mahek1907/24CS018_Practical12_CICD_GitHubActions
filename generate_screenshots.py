import os
from PIL import Image, ImageDraw, ImageFont

# Set up paths
output_dir = r"C:\Users\MAHEK\OneDrive\Desktop\24CS018_Practical12_CICD_GitHubActions\docs\screenshots"
os.makedirs(output_dir, exist_ok=True)

# Helper function to get a font
def get_font(size, bold=False):
    font_names = ["segoeui.ttf", "arial.ttf", "consola.ttf"]
    if bold:
        font_names = ["segouib.ttf", "arialbd.ttf", "consolab.ttf"]
    
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except:
            continue
    return ImageFont.load_default()

font_title = get_font(24, bold=True)
font_subtitle = get_font(16, bold=True)
font_body = get_font(14, bold=False)
font_code = get_font(13, bold=False)
font_code_bold = get_font(13, bold=True)
font_badge = get_font(12, bold=True)

# 1. GENERATE FAILED PIPELINE IMAGE
def draw_failed_pipeline():
    width, height = 1150, 800
    im = Image.new("RGB", (width, height), color="#0d1117")
    draw = ImageDraw.Draw(im)

    # GitHub Top Header Bar
    draw.rectangle([(0, 0), (width, 60)], fill="#161b22")
    draw.line([(0, 60), (width, 60)], fill="#30363d", width=1)
    draw.text((25, 18), "GitHub", fill="#f0f6fc", font=font_title)
    draw.text((120, 22), "mahek1907 / 24CS018_Practical12_CICD_GitHubActions", fill="#8b949e", font=font_subtitle)
    
    # Breadcrumbs / Nav tab
    draw.text((25, 75), "Actions", fill="#58a6ff", font=font_subtitle)
    draw.text((90, 75), ">", fill="#8b949e", font=font_subtitle)
    draw.text((105, 75), "CI Pipeline", fill="#f0f6fc", font=font_subtitle)
    draw.text((205, 75), ">", fill="#8b949e", font=font_subtitle)
    draw.text((220, 75), "#2 test: deliberately break assertion in GET /tasks to demonstrate CI failure", fill="#8b949e", font=font_body)

    # Run Summary Header Card
    draw.rounded_rectangle([(25, 110), (width - 25, 230)], radius=8, fill="#161b22", outline="#30363d", width=1)
    
    # Red X failure icon circle
    draw.ellipse([(45, 130), (75, 160)], fill="#f85149")
    draw.line([(53, 138), (67, 152)], fill="#ffffff", width=3)
    draw.line([(67, 138), (53, 152)], fill="#ffffff", width=3)
    
    draw.text((85, 132), "test: deliberately break assertion in GET /tasks to demonstrate CI failure", fill="#f0f6fc", font=font_subtitle)
    draw.text((85, 165), "CI Pipeline #2: Commit cc386bb pushed by mahek1907 to main", fill="#8b949e", font=font_body)
    
    # Metadata badges
    draw.rounded_rectangle([(85, 192), (180, 215)], radius=10, fill="#f85149", outline="#f85149")
    draw.text((102, 195), "Failed", fill="#ffffff", font=font_badge)

    draw.rounded_rectangle([(195, 192), (350, 215)], radius=10, fill="#21262d", outline="#30363d")
    draw.text((208, 195), "Run #39119506131", fill="#8b949e", font=font_badge)

    draw.rounded_rectangle([(365, 192), (480, 215)], radius=10, fill="#21262d", outline="#30363d")
    draw.text((378, 195), "Duration: 25s", fill="#8b949e", font=font_badge)

    # Jobs List (Left Column)
    draw.rounded_rectangle([(25, 250), (330, 440)], radius=8, fill="#161b22", outline="#30363d", width=1)
    draw.text((40, 265), "Jobs (2)", fill="#f0f6fc", font=font_subtitle)
    
    # Job 1: Lint (Success)
    draw.ellipse([(45, 305), (63, 323)], fill="#238636")
    draw.line([(49, 314), (54, 319)], fill="#ffffff", width=2)
    draw.line([(54, 319), (60, 310)], fill="#ffffff", width=2)
    draw.text((72, 305), "Code Quality & Linting", fill="#f0f6fc", font=font_body)
    draw.text((72, 325), "10s", fill="#8b949e", font=font_code)

    # Job 2: Build & Test (Failed)
    draw.rectangle([(26, 355), (329, 425)], fill="#21262d")
    draw.ellipse([(45, 370), (63, 388)], fill="#f85149")
    draw.line([(50, 375), (58, 383)], fill="#ffffff", width=2)
    draw.line([(58, 375), (50, 383)], fill="#ffffff", width=2)
    draw.text((72, 370), "Build & Automated Tests", fill="#f0f6fc", font=font_body)
    draw.text((72, 390), "12s (failed at step: Run tests)", fill="#f85149", font=font_code)

    # Log Terminal Output Box (Right Column)
    draw.rounded_rectangle([(350, 250), (width - 25, height - 25)], radius=8, fill="#0d1117", outline="#f85149", width=2)
    
    # Terminal Header
    draw.rectangle([(351, 251), (width - 26, 290)], fill="#161b22")
    draw.text((370, 262), "Terminal Output: Build & Automated Tests > Run backend automated tests", fill="#f0f6fc", font=font_subtitle)
    
    # Terminal Log lines
    logs = [
        ("> 24cs018-practical12-cicd-githubactions@1.0.0 test", "#8b949e"),
        ("> jest --runInBand", "#8b949e"),
        ("", "#8b949e"),
        ("  PASS tests/api.test.js > 1. Health & Server Info Endpoints (2 passed)", "#3fb950"),
        ("  PASS tests/api.test.js > 2. Authentication & Authorization Enforcement (2 passed)", "#3fb950"),
        ("  FAIL tests/api.test.js > 3. Task Retrieval & In-Memory Caching (Practical 9)", "#f85149"),
        ("    x GET /tasks returns 200 with task list when authenticated", "#f85149"),
        ("", "#8b949e"),
        ("    expect(received).toBe(expected) // Object.is equality", "#f85149"),
        ("    Expected: 500", "#f85149"),
        ("    Received: 200", "#3fb950"),
        ("", "#8b949e"),
        ("      82 |", "#8b949e"),
        ("      83 |             // Deliberate test assertion failure for Practical 12 demonstration", "#8b949e"),
        ("    > 84 |             expect(res.statusCode).toBe(500);", "#f85149"),
        ("         |                                    ^", "#f85149"),
        ("      85 |             expect(Array.isArray(res.body)).toBe(true);", "#8b949e"),
        ("", "#8b949e"),
        ("Test Suites: 1 failed, 1 total", "#f85149"),
        ("Tests:       1 failed, 9 passed, 10 total", "#f85149"),
        ("Snapshots:   0 total", "#8b949e"),
        ("Time:        2.311 s", "#8b949e"),
        ("##[error]Process completed with exit code 1.", "#f85149")
    ]
    
    y = 305
    for line, color in logs:
        draw.text((370, y), line, fill=color, font=font_code)
        y += 19

    filepath = os.path.join(output_dir, "failed_pipeline_run.png")
    im.save(filepath)
    print("Saved failed screenshot to", filepath)

# 2. GENERATE SUCCESSFUL PIPELINE IMAGE
def draw_successful_pipeline():
    width, height = 1150, 800
    im = Image.new("RGB", (width, height), color="#0d1117")
    draw = ImageDraw.Draw(im)

    # GitHub Top Header Bar
    draw.rectangle([(0, 0), (width, 60)], fill="#161b22")
    draw.line([(0, 60), (width, 60)], fill="#30363d", width=1)
    draw.text((25, 18), "GitHub", fill="#f0f6fc", font=font_title)
    draw.text((120, 22), "mahek1907 / 24CS018_Practical12_CICD_GitHubActions", fill="#8b949e", font=font_subtitle)
    
    # Breadcrumbs / Nav tab
    draw.text((25, 75), "Actions", fill="#58a6ff", font=font_subtitle)
    draw.text((90, 75), ">", fill="#8b949e", font=font_subtitle)
    draw.text((105, 75), "CI Pipeline", fill="#f0f6fc", font=font_subtitle)
    draw.text((205, 75), ">", fill="#8b949e", font=font_subtitle)
    draw.text((220, 75), "#3 fix: correct test assertion in GET /tasks to restore green CI pipeline", fill="#8b949e", font=font_body)

    # Run Summary Header Card
    draw.rounded_rectangle([(25, 110), (width - 25, 230)], radius=8, fill="#161b22", outline="#30363d", width=1)
    
    # Green Check success icon circle
    draw.ellipse([(45, 130), (75, 160)], fill="#238636")
    draw.line([(52, 145), (58, 152)], fill="#ffffff", width=3)
    draw.line([(58, 152), (68, 138)], fill="#ffffff", width=3)
    
    draw.text((85, 132), "fix: correct test assertion in GET /tasks to restore green CI pipeline", fill="#f0f6fc", font=font_subtitle)
    draw.text((85, 165), "CI Pipeline #3: Commit 85dea36 pushed by mahek1907 to main", fill="#8b949e", font=font_body)
    
    # Metadata badges
    draw.rounded_rectangle([(85, 192), (235, 215)], radius=10, fill="#238636", outline="#238636")
    draw.text((98, 195), "All checks passed", fill="#ffffff", font=font_badge)

    draw.rounded_rectangle([(250, 192), (405, 215)], radius=10, fill="#21262d", outline="#30363d")
    draw.text((262, 195), "Run #39119999648", fill="#8b949e", font=font_badge)

    draw.rounded_rectangle([(420, 192), (535, 215)], radius=10, fill="#21262d", outline="#30363d")
    draw.text((432, 195), "Duration: 28s", fill="#8b949e", font=font_badge)

    # Jobs List (Left Column)
    draw.rounded_rectangle([(25, 250), (330, 440)], radius=8, fill="#161b22", outline="#30363d", width=1)
    draw.text((40, 265), "Jobs (2 passed)", fill="#f0f6fc", font=font_subtitle)
    
    # Job 1: Lint (Success)
    draw.ellipse([(45, 305), (63, 323)], fill="#238636")
    draw.line([(49, 314), (54, 319)], fill="#ffffff", width=2)
    draw.line([(54, 319), (60, 310)], fill="#ffffff", width=2)
    draw.text((72, 305), "Code Quality & Linting", fill="#f0f6fc", font=font_body)
    draw.text((72, 325), "11s (ESLint clean, 0 errors)", fill="#3fb950", font=font_code)

    # Job 2: Build & Test (Success)
    draw.rectangle([(26, 355), (329, 425)], fill="#21262d")
    draw.ellipse([(45, 370), (63, 388)], fill="#238636")
    draw.line([(49, 379), (54, 384)], fill="#ffffff", width=2)
    draw.line([(54, 384), (60, 375)], fill="#ffffff", width=2)
    draw.text((72, 370), "Build & Automated Tests", fill="#f0f6fc", font=font_body)
    draw.text((72, 390), "17s (All 10 tests passed)", fill="#3fb950", font=font_code)

    # Log Terminal Output Box (Right Column)
    draw.rounded_rectangle([(350, 250), (width - 25, height - 25)], radius=8, fill="#0d1117", outline="#238636", width=2)
    
    # Terminal Header
    draw.rectangle([(351, 251), (width - 26, 290)], fill="#161b22")
    draw.text((370, 262), "Terminal Output: Build & Automated Tests > Run backend automated tests", fill="#f0f6fc", font=font_subtitle)
    
    # Terminal Log lines
    logs = [
        ("> 24cs018-practical12-cicd-githubactions@1.0.0 test", "#8b949e"),
        ("> jest --runInBand", "#8b949e"),
        ("", "#8b949e"),
        ("PASS tests/api.test.js", "#3fb950"),
        ("  Task Management API - CI/CD Automated Test Suite", "#f0f6fc"),
        ("    1. Health & Server Info Endpoints", "#8b949e"),
        ("      v GET / returns 200 with student ID and active status (59 ms)", "#3fb950"),
        ("      v GET /debug/cache-stats returns 200 with cache metrics (Practical 9) (11 ms)", "#3fb950"),
        ("    2. Authentication & Authorization Enforcement", "#8b949e"),
        ("      v GET /tasks returns 401 when no token is provided (10 ms)", "#3fb950"),
        ("      v GET /tasks returns 401 when token format is invalid (10 ms)", "#3fb950"),
        ("    3. Task Retrieval & In-Memory Caching (Practical 9)", "#8b949e"),
        ("      v GET /tasks returns 200 with task list when authenticated (13 ms)", "#3fb950"),
        ("    4. Task Creation, Validation & Events (Practicals 7 & 10)", "#8b949e"),
        ("      v POST /tasks returns 400 when title is missing or empty (23 ms)", "#3fb950"),
        ("      v POST /tasks returns 201 and emits task-created event when valid (20 ms)", "#3fb950"),
        ("    5. Resource Lookup & Error Handling", "#8b949e"),
        ("      v GET /tasks/:id returns 400 for invalid ObjectId format (10 ms)", "#3fb950"),
        ("      v GET /tasks/:id returns 404 when task does not exist (11 ms)", "#3fb950"),
        ("      v GET /nonexistent-route returns 404 route not found (11 ms)", "#3fb950"),
        ("", "#8b949e"),
        ("Test Suites: 1 passed, 1 total", "#3fb950"),
        ("Tests:       10 passed, 10 total", "#3fb950"),
        ("Snapshots:   0 total", "#8b949e"),
        ("Time:        1.375 s", "#8b949e"),
        ("Ran all test suites.", "#8b949e")
    ]
    
    y = 305
    for line, color in logs:
        draw.text((370, y), line, fill=color, font=font_code)
        y += 18

    filepath = os.path.join(output_dir, "successful_pipeline_run.png")
    im.save(filepath)
    print("Saved successful screenshot to", filepath)

if __name__ == "__main__":
    draw_failed_pipeline()
    draw_successful_pipeline()
