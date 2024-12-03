def generate_test_cases(parsed_data):
    """
    Generate structured test cases from parsed user story data.
    """
    actions = parsed_data.get("actions", [])
    actors = parsed_data.get("actors", [])

    test_cases = []
    for idx, action in enumerate(actions, start=1):
        for actor in actors:
            test_cases.append({
                "ID": idx,
                "Step": f"{actor} performs '{action}'",
                "Expected": "Action completes successfully"
            })
            test_cases.append({
                "ID": idx + 1,
                "Step": f"{actor} performs '{action}' with invalid input",
                "Expected": "Appropriate error message displayed"
            })
    return test_cases
