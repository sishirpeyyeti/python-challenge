import csv

def analyze_election_data(file_path, output_folder):
    total_votes = 0
    candidate_votes = {}

    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            total_votes += 1
            candidate = row[2]

            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    output_file_path = f'{output_folder}/election_results.txt'

    with open(output_file_path, 'w') as output_file:
        output_file.write("Total Votes: {}\n".format(total_votes))
        output_file.write("-------------------------\n")

        output_file.write("List of Candidates:\n")
        for candidate in candidate_votes:
            output_file.write(f"{candidate}\n")

        output_file.write("-------------------------\n")

        output_file.write("Percentage of Votes Each Candidate Won:\n")
        for candidate in candidate_votes:
            percentage = (candidate_votes[candidate] / total_votes) * 100
            output_file.write("{}: {:.2f}%\n".format(candidate, percentage))

        output_file.write("-------------------------\n")

        winner = max(candidate_votes, key=candidate_votes.get)
        output_file.write("Winner: {}\n".format(winner))
        output_file.write("-------------------------\n")

    print(f"Results exported to: {output_file_path}")


analyze_election_data('PyPoll\Resources\election_data.csv', 'PyPoll\Analysis')
