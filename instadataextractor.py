import instaloader

# Creating an object
ig = instaloader.Instaloader()

# Taking Instagram username 
username = input("Enter the Username (i.e. prashon10): ")

profile = instaloader.Profile.from_username(ig.context,username)

print("Username: ",profile.username)
print("No. of posts: ",profile.mediacount)
print(profile.username+"is having "+str(profile.followers)+" followers.")
print(profile.username+"is following "+str(profile.followees)+" peoples.")
print("Bio: ",profile.biography)
print()
instaloader.Instaloader().download_profile(username,profile_pic_only=True)