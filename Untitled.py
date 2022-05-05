#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[2]:


print ("pooja")


# In[3]:


export GIT_PARENT_DIR=~
export GIT_REPO_NAME= Jupyter_DataScience
export GIT_BRANCH_NAME= master
export GIT_USER= Pooja Das
export GIT_EMAIL= Poojadas93@outlook.com
export GITHUB_ACCESS_TOKEN= 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
export GIT_USER_UPSTREAM= PoojaDas


# In[ ]:


####################### SSH KEY FOR GIT ###################################
eval `ssh-agent -s` && ssh-add -k
####################### To be added to git account settings ################


###################### GIT PARAMETERS #####################################
export GIT_PARENT_DIR=~
export GIT_REPO_NAME=Jupyter_DataScience
export GIT_BRANCH_NAME= master
export GIT_USER=PoojaDasIndia
export GIT_EMAIL=Poojadigitechindia@gmail.com
export GITHUB_ACCESS_TOKEN=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
export GIT_USER_UPSTREAM=PoojaDas



############################################################################
#### DO NOT EDIT BELOW THIS LINE: derived variables
############################################################################

export GIT_REMOTE_URL=git@github.com:$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_URL_HTTPS=https://github.com/$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_UPSTREAM=$GIT_USER_UPSTREAM/$GIT_REPO_NAME


####################### Git Repo where notebooks will be pushed ############
cd $GIT_PARENT_DIR && git clone $GIT_REMOTE_URL_HTTPS



####################### Change in jupyter config ###########################
if [ ! -f ~/.jupyter/jupyter_notebook_config.py ]; then
   jupyter notebook --generate-config
fi

echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyter/jupyter_notebook_config.py

cp $GIT_PARENT_DIR/githubcommit/config ~/.ssh/config

