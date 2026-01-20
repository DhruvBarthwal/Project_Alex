export async function  sendMessage(text: string, emailId : string | null){
    console.log("API CALL → text:", text, "email_id:", emailId);

    const res = await fetch("http://localhost:8000/voice", {
    method : "POST",
    headers : {"Content-Type" : "application/json"},
    body: JSON.stringify({
        text,
        email_id : emailId,
    }),
    });

    if(!res.ok){
        throw new Error("Backend error");
    }

    return res.json();
}