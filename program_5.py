def main():
    courses = {}  # Dictionary to store course ID as key and course name as value

    # Input loop for courses
    print("Enter course IDs and names. Type 'done' when finished.")
    while True:
        course_id = input("Enter course ID (or 'done' to stop): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ")

        # Add the course to the dictionary
        courses[course_id] = course_name

    # Ask the user for a subject to filter courses by
    subject = input("Enter the subject (e.g., 'COS') to filter courses by: ")

    # Display courses matching the subject
    print(f"\nCourses with the subject '{subject}':")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):  # Check if course ID starts with the given subject
            print(f"{course_id}: {course_name}")


if __name__ == "__main__":
    main()
