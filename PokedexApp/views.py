from django.shortcuts import render
from .connect import gen9_collection
from bson.objectid import ObjectId
from bson import json_util
from datetime import datetime
from django.http import JsonResponse
from django.http import QueryDict
import json

from django.views.decorators.csrf import csrf_exempt

def home(request):
    count = gen9_collection.count_documents({})
    response = {"data": {"count": count}, "message": "successful"}
    return JsonResponse(response, status=200)

def add_pokemon(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        data = json.loads(body)

        new_user = {
            "num": data.get("num"),
            "name": data.get("name"),
            "type1": data.get("type1"),
            "type2": data.get("type2"),
            "ability": data.get("ability"),
            "hid_ability": data.get("hid_ability"),
            "category": data.get("category"),
            "info_en": data.get("info_en"),
            "info_vn": data.get("info_vn"),
            "image": data.get("image"),
            "icon": data.get("icon"),
        }

        if new_user.get("num") and new_user.get("name") and new_user.get("type1") and new_user.get("type2") and new_user.get("ability") and new_user.get("hid_ability") and new_user.get("category") and new_user.get("info_en") and new_user.get("info_vn") and new_user.get("image") and new_user.get("icon"):
            result = gen9_collection.insert_one(new_user)

            if result.inserted_id:
                return JsonResponse({"message": "Created pokemon successfully"})

        return JsonResponse({"error": "Failed to create new pokemon"}, status=404)
        
    return JsonResponse({"error": "Invalid request method"}, status=405)

def gen9(request):
    if request.method == "GET":
        data = []
        data = gen9_collection.find({})
        data = json.loads(json_util.dumps(data))
        data_res = []
        for ele in data:
            data_res += [ele]
        response = {"data": data_res, "message": "successful"}
        return JsonResponse(response, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# def worker(request):
#     if request.method == "GET":
#         data = []
#         data = users_collection.find({"$or":[{"role": "Worker"}]})
#         data = json.loads(json_util.dumps(data))
#         data_res = []
#         for ele in data:
#             data_res += [ele]
#         response = {"data": data_res, "message": "successful"}
#         return JsonResponse(response, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# def create_job(request):
#     if request.method == "POST":
#         body = request.body.decode("utf-8")
#         data = json.loads(body)

#         requirement = data.get("requirement")
#         image = data.get("image")

#         new_job = {
#             "owner_id": data.get("owner_id"),
#             "name": data.get("name"),
#             "desc": data.get("desc"),
#             "datetime": data.get("datetime"),
#             "address": data.get("address"),
#             "salary": data.get("salary"),
#             "email": data.get("email"),
#             "phone_num": data.get("phone_num"),
#             "requirement": requirement if requirement else "",
#             "image": image if image else "",
#         }

#         if new_job.get("owner_id") and new_job.get("name") and new_job.get("desc") and new_job.get("datetime") and new_job.get("address") and new_job.get("salary"):
#             result = jobs_collection.insert_one(new_job)

#             if result.inserted_id:
#                 return JsonResponse({"message": "Created job successfully"})

#         return JsonResponse({"error": "Failed to create new job"}, status=404)
        
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def get_job_info(request, id):
#     if request.method == "GET":     
#         job = jobs_collection.find_one({"_id": ObjectId(id)})
        
#         if job:
#             return JsonResponse({
#                 "message": "Job found",
#                 "data": {
#                     "owner_id": job.get("owner_id"),
#                     "name": job.get("name"),
#                     "desc": job.get("desc"),
#                     "datetime": job.get("datetime"),
#                     "address": job.get("address"),
#                     "salary": job.get("salary"),
#                     "email": job.get("email"),
#                     "phone_num": job.get("phone_num"),
#                     "requirement": job.get("requirement"),
#                     "image": job.get("image")
#                 }
#             })
#         return JsonResponse({"error": "Job not found"}, status=404)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def my_job(request, id):
#     if request.method == "GET":
#         try:
#             data = []
#             data = jobs_collection.find({"owner_id": id})
#             data = json.loads(json_util.dumps(data))
#             data_res = []
#             for ele in data:
#                 data_res += [ele]
#             response = {"data": data_res, "message": "successful"}
#             return JsonResponse(response, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# def delete_job(request, id):
#     if request.method == "DELETE":
#         cv = jobs_collection.find_one({"_id": ObjectId(id)})
#         if cv:
#             # Assuming you are using pymongo or a similar library
#             result = jobs_collection.delete_one({"_id": ObjectId(id)})
#             if result.deleted_count > 0:
#                 return JsonResponse({"message": "Job deleted successfully"})
        
#         return JsonResponse({"error": "Invalid job id"}, status=404)
    
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def job(request):
#     if request.method == "GET":
#         data = []
#         data = jobs_collection.find({})
#         data = json.loads(json_util.dumps(data))
#         data_res = []
#         for ele in data:
#             data_res += [ele]
#         response = {"data": data_res, "message": "successful"}
#         return JsonResponse(response, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# def create_cv(request):
#     if request.method == "POST":
#         body = request.body.decode("utf-8")
#         data = json.loads(body)

#         exp = data.get("exp")
#         certificates = data.get("certificate")
#         certificate_ids = []  # Store generated skill IDs
#         if isinstance(certificates, list):
#             for certificate in certificates:
#                 certificate_id = str(ObjectId())
#                 certificate_ids.append({"certificate_id": certificate_id, "name": certificate})
#             # certificates = [certificates] if certificates else []
#         skills = data.get("skill")
#         skill_ids = []  # Store generated skill IDs
#         if isinstance(skills, list):
#             for skill in skills:
#                 skill_id = str(ObjectId())
#                 name = skill.get("name")
#                 skill_ids.append({"skill_id": skill_id, "name": name if name else "", "skillId": skill.get("skillId"), "experienceYear": skill.get("experienceYear")})
#         new_cv = {
#             "worker_id": data.get("worker_id"),
#             "name": data.get("name"),
#             "intro": data.get("intro"),
#             "skill": skill_ids,
#             "certificate": certificate_ids if certificate_ids else "",
#             "exp": exp if exp else "",
#         }

#         if new_cv.get("worker_id") and new_cv.get("name") and new_cv.get("intro") and new_cv.get("skill"):
#             result = cvs_collection.insert_one(new_cv)

#             if result.inserted_id:
#                 return JsonResponse({"message": "Created cv successfully"})

#         return JsonResponse({"error": "Failed to create new cv"}, status=404)
        
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def get_cv_info(request, id):
#     if request.method == "GET":     
#         cv = cvs_collection.find_one({"worker_id": id})
        
#         if cv:
#             return JsonResponse({
#                 "message": "CV found",
#                 "data": {
#                     "worker_id": cv.get("worker_id"),
#                     "name": cv.get("name"),
#                     "intro": cv.get("intro"),
#                     "skill": cv.get("skill"),
#                     "certificate": cv.get("certificate"),
#                     "exp": cv.get("exp"),
#                 }
#             })
#         return JsonResponse({"message": "CV not found"})

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# # NOT DONE
# def update_cv(request):
#     if request.method == "POST":
#         body = request.body.decode("utf-8")
#         data = json.loads(body)
#         updated_cv = {}
#         cv = cvs_collection.find_one({"worker_id": data.get("id")})
#         data.pop("id")
#         if cv:
#             if not data.get("name"):
#                 data["name"] = cv.get("name")
#             if not data.get("intro"):
#                 data["intro"] = cv.get("intro")
#             if "skill" in data:
#                 if isinstance(data["skill"], list):
#                     cv["skill"] = data["skill"]
#                 else:
#                     cv["skill"].append(data["skill"])  # Assuming skill is updated with a single value
#                 data.pop("skill")

#             if "certificate" in data:
#                 if isinstance(data["certificate"], list):
#                     cv["certificate"] = data["certificate"]
#                 else:
#                     cv["certificate"].append(data["certificate"])  # Assuming certificate is updated with a single value
#                 data.pop("certificate")
#             if not data.get("exp"):
#                 data["exp"] = cv.get("exp")
#             change = {"$set": data}
#             result = cvs_collection.update_one(cv, change)           
#             if result:
#                 return JsonResponse({"message": "Updated successfully"})
#         return JsonResponse({"error": "Invalid cv id"}, status=404)
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def delete_cv(request, id):
#     if request.method == "DELETE":
#         cv = cvs_collection.find_one({"worker_id": id})
#         if cv:
#             # Assuming you are using pymongo or a similar library
#             result = cvs_collection.delete_one({"worker_id": id})
#             if result.deleted_count > 0:
#                 return JsonResponse({"message": "CV deleted successfully"})
        
#         return JsonResponse({"error": "Invalid worker id"}, status=404)
    
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def cv(request):
#     if request.method == "GET":
#         data = []
#         data = cvs_collection.find({})
#         data = json.loads(json_util.dumps(data))
#         data_res = []
#         for ele in data:
#             data_res += [ele]
#         response = {"data": data_res, "message": "successful"}
#         return JsonResponse(response, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# def create_skill(request):
#     if request.method == "POST":
#         body = request.body.decode("utf-8")
#         data = json.loads(body)

#         new_skill = {
#             "name": data.get("name"),
#         }

#         if new_skill.get("name"):
#             result = skills_collection.insert_one(new_skill)

#             if result.inserted_id:
#                 return JsonResponse({"message": "Created skill successfully"})

#         return JsonResponse({"error": "Failed to create new skill"}, status=404)
        
#     return JsonResponse({"error": "Invalid request method"}, status=405)

# def skill(request):
#     if request.method == "GET":
#         data = []
#         data = skills_collection.find({})
#         data = json.loads(json_util.dumps(data))
#         data_res = []
#         for ele in data:
#             data_res += [ele]
#         response = {"data": data_res, "message": "successful"}
#         return JsonResponse(response, status=200)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
