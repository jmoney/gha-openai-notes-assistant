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
                chat_completion = openai.ChatCompletion.create(
                    model="gpt-4", 
                    max_tokens=1000,
                    temperature=0.7, 
                    messages=[{"role": "user", "content": prompt_template.format(completed_tasks=content)}])
                output = {}
                output["content"] = chat_completion.choices[0].message.content
                print(json.dumps(output))
        else:
            print("Unknown assistant", file=sys.stderr)
            sys.exit(1)
