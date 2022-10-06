

# def ValidateAuthenticationToken(func):
# 	def JWTcheck(*args, **kwargs):
# 		request = args[0]
# 		auth = get_authorization_header(request).split()
# 		if not auth or auth[0].lower() != b'bearer':
# 			raise AuthenticationFailed({"success": "0", "message": "Please provide token"})
# 		if len(auth) == 1:
# 			raise AuthenticationFailed({"success": "0", "message": "Please provide token"})
# 		elif len(auth) > 2:
# 			raise AuthenticationFailed({"success": "0", "message": "Please provide token"})
# 		try:
# 			token = auth[1]
# 			if token == "null":
# 				raise AuthenticationFailed({"success": "0", "message": "Invalid token header"})
# 			usr = authenticate_credentials(token)
# 			user = User.objects.get(id=int(usr))
# 			if not user.verified:
# 				raise AuthenticationFailed({"success": "0", "message": "Please verify your email"})
# 			else:
# 				current_time = timezone.now()
# 				if user.token_usage_datetime is not None:
# 					allowed_request_interval = user.token_usage_datetime + datetime.timedelta(seconds=3600)
# 					if current_time > allowed_request_interval:
# 						user.session_expired = True
# 						user.user_agent = getBrowserDetails(request)
# 						user.token_usage_ip = getIp(request)
# 						user.save()
# 						raise AuthenticationFailed({"success": "3", "message": "Session Expired"})
# 				kwargs['user'] = user
# 				user.token_usage_datetime = datetime.datetime.now()
# 				user.save()
# 		except UnicodeError:
# 			raise AuthenticationFailed({"success": "0", "message": "Invalid token"})
# 		return func(*args, **kwargs)

# 	return JWTcheck
