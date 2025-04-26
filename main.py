import argparse
import json
import openai
import sys

if __name__ == "__main__":

    prog = argparse.ArgumentParser()
    prog.add_argument("--assistant", help="Notes Assistant", required=True, action="store", dest="assistant")
    prog.add_argument("--file", help="File to process", required=True, action="store", dest="file")
    prog.add_argument("--prompts-dir", help="Directory containing prompts", required=True, action="store", dest="prompts_dir")
    args = prog.parse_args()

    with(open(args.file, "r")) as f:
        content = f.read() 
        if args.assistant == "quarterly_review":
            with(open(f"{args.prompts_dir}/quarterly_summary.txt", "r")) as f:
                prompt_template = f.read()
                work = json.loads(content)
                for item in work:       
                    chat_completion = openai.ChatCompletion.create(
                        model="gpt-4o-2024-08-06", 
                        max_tokens=10000,
                        temperature=0.7, 
                        messages=[{"role": "user", "content": prompt_template.format(completed_tasks=json.dumps(work[item]))}])
                    output = {}
                    output[f"{item}_content"] = chat_completion.choices[0].message.content
                summary = ""
                for value in output:
                    summary += output[value]
                    summary += "\n"
                print(json.dumps({"content": summary}))
        elif args.assistant == "weekly_review":
            with(open(f"{args.prompts_dir}/weekly_summary.txt", "r")) as f:
                prompt_template = f.read()
                work = json.loads(content)
                for item in work:       
                    chat_completion = openai.ChatCompletion.create(
                        model="gpt-4o-2024-08-06", 
                        max_tokens=10000,
                        temperature=0.7, 
                        messages=[{"role": "user", "content": prompt_template.format(completed_tasks=json.dumps(work[item]))}])
                    output = {}
                    output[f"{item}_content"] = chat_completion.choices[0].message.content
                summary = ""
                for value in output:
                    summary += output[value]
                    summary += "\n"
                print(json.dumps({"content": summary}))

        else:
            print("Unknown assistant", file=sys.stderr)
            sys.exit(1)
