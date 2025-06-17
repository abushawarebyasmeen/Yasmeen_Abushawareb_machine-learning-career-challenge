from django.shortcuts import render
from .helper.query import query_groq
from .models import FAQ, InteractionLog
from .helper.embeddings import generate_embedding, compute_similarity, initialize_faq_embeddings
from .helper.google_search import search_in_urls

PREFERRED_URLS = [
    # ... aynı linkler ...
]

def home(request):
    initialize_faq_embeddings()  # İstersen burada veya yönetici panelinden çağırabilirsin
    return render(request, "home.html")

def ask_question(request):
    user_query = request.GET.get("query")
    if not user_query:
        return render(request, "ask.html", {
            "error": "Soru girilmedi. Lütfen geri dönüp bir soru yazın.",
        })

    query_embedding = generate_embedding(user_query)
    faqs = FAQ.objects.all()

    faq_data = [(faq.embedding, faq.question, faq.answer) for faq in faqs if faq.embedding]

    if faq_data:
        faq_embeddings, faq_questions, faq_answers = zip(*faq_data)
        similarity_scores = compute_similarity(query_embedding, faq_embeddings)

        max_index, max_similarity = max(enumerate(similarity_scores), key=lambda x: x[1])

        if max_similarity >= 0.6:
            response = faq_answers[max_index]
            suggestions = []
        else:
            preferred_result = search_in_urls(user_query, PREFERRED_URLS)

            if preferred_result:
                full_query = f"Lütfen şu soruya Türkçe ve kısa bir cevap ver: {user_query} {preferred_result}"
                response = query_groq(full_query)
                suggestions = []
            else:
                response = "Üzgünüm, bu soruya şu anda bir yanıt bulamadım."
                top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
                suggestions = [faq_questions[i] for i in top_indices if similarity_scores[i] > 0.3]

            InteractionLog.objects.create(user_query=user_query, response=response)
    else:
        preferred_result = search_in_urls(user_query, PREFERRED_URLS)

        if preferred_result:
            full_query = f"Lütfen şu soruya Türkçe ve kısa bir cevap ver: {user_query} {preferred_result}"
            response = query_groq(full_query)
            suggestions = []
        else:
            response = "Üzgünüm, bu soruya şu anda bir yanıt bulamadım."
            suggestions = []

        InteractionLog.objects.create(user_query=user_query, response=response)

    return render(request, "ask.html", {
        "query": user_query,
        "response": response,
        "suggestions": suggestions,
    })