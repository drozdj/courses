def clean_transcript(input_file, output_file, paragraph_interval=5):
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Initialize list for cleaned lines
        cleaned_lines = []
        
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
                
            # Skip timestamp lines
            if line.strip().replace(':', '').replace('.', '').isdigit():
                continue
                
            cleaned_lines.append(line.strip())

        # Write to output file with paragraph breaks
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, cleaned_line in enumerate(cleaned_lines):
                f.write(cleaned_line + '\n')
                # Add extra newline every paragraph_interval lines
                if (i + 1) % paragraph_interval == 0:
                    f.write('\n')
                    
        print(f"Successfully cleaned transcript. Output saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


input_file = "transcript.txt"
output_file = "cleaned_transcript.txt"
clean_transcript(input_file, output_file, paragraph_interval=3)  # Creates a new paragraph every 3 lines