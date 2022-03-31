# from flask import  Response, request, jsonify
# from flask_restful import Resource
# from flask_mongoengine import json
# from Main.Model.Transaction import Transaction
# from Main.Model.User import User
# from Main.Model.UserTransactionDetails import UserTransactionDetails as UTD

# class TransactionApi(Resource):
        
#     def post(self):
#         #create new transaction for the auth user
#         body = request.get_json()
#         username = body.pop('username')
#         ttype = body.pop('type')
#         user = User.objects(username=username).first()
#         T = Transaction(**body).save()

#         UTD(User = user, Transaction = T, Type = ttype).save() 
#         transac=[]
#         UT = UTD.objects.filter(User__in = [user.id])
#         leng = len(UT)
#         for i in range(leng):
#             if UT[i].Type.lower() == 'expense':
#                 amt = -1 * (float(UT[i].Transaction.amount))
#                 transac.append(amt)
#             else:
#                 transac.append(float(UT[i].Transaction.amount))
#         user.update(balance=sum(transac))
#         return {'Response:': str(ttype)+' added sucessfully !!'}, 200

# class GetTransactionApi(Resource):
#     def post(self):
#         body = request.get_json()
#         username = body.pop('username')
#         user = User.objects(username=username).first()
#         UT = UTD.objects.filter(User__in = [user.id])
#         leng = len(UT)
#         data = []
#         for i in range(leng):
#             data.append({
#                 "date": UT[i].Transaction.Tdate,
#                 "amount": UT[i].Transaction.amount,
#                 "category": UT[i].Transaction.category,
#                 "description": UT[i].Transaction.description,
#                 "currency": UT[i].Transaction.currency,
#                 "type": UT[i].Type,
#             })
#         return jsonify(data)  
    