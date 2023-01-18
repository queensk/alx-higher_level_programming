git filter-branch --commit-filter '
        if [ "$GIT_COMMITTER_NAME" = "Old Name" ];
        then
                GIT_COMMITTER_NAME="New Name";
                GIT_AUTHOR_NAME="New Name";
                GIT_COMMITTER_EMAIL="newemail@example.com";
                GIT_AUTHOR_EMAIL="newemail@example.com";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
