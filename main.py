import logging #logging module
from services.gmail_api_service import send_email_gmail_api
from file_automation import organize_files #Download folder organize krse fun
from report_generator import generate_report #report generate

def main(): #main fun
    logging.basicConfig(level=logging.INFO)

    print("== Automation Tool Started ==")
    
    #file automation
    organize_files() #Download folder scan krine file move krse

    # Report generation
    report_path, email_list = generate_report()

    #Email API services
    if report_path and email_list: #vailable che k ny check krse
        for email in email_list:
            if "@" not in email: #invalid email skip
                print(f"Skipping invalid email: {email}")
                continue

            send_email_gmail_api(
                to_email=email,
                subject="Monthly Sales Report",
                text_body=(
                    "Hello,\n\n"
                    "Please find the attached sales report.\n\n"
                    "Regards,\nAutomation Tool"
                ),
                attachments=[report_path],
            )
        print(f"Gmail sent to {email}")

    print(" Automation Tool Finish")

if __name__ == "__main__":
    main()#dorect run thay to main() chalse
