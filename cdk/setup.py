import setuptools

with open("README.md") as fp:
    long_description = fp.read()

# this is also set in setup-env.sh
CDK_VERSION="1.87.1"

setuptools.setup(
    name="wordpress",
    version="1.0.0",

    description="AWS Marketplace Pattern for WordPress by Ordinary Experts.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Ordinary Experts",

    package_dir={"": "wordpress"},
    packages=setuptools.find_packages(where="wordpress"),

    install_requires=[
        f"aws-cdk.aws-autoscaling=={CDK_VERSION}",
        f"aws-cdk.aws-cloudformation=={CDK_VERSION}",
        f"aws-cdk.aws-cloudwatch=={CDK_VERSION}",
        f"aws-cdk.aws-codebuild=={CDK_VERSION}",
        f"aws-cdk.aws-codedeploy=={CDK_VERSION}",
        f"aws-cdk.aws-codepipeline-actions=={CDK_VERSION}",
        f"aws-cdk.aws-codepipeline=={CDK_VERSION}",
        f"aws-cdk.aws-ec2=={CDK_VERSION}",
        f"aws-cdk.aws-efs=={CDK_VERSION}",
        f"aws-cdk.aws-elasticloadbalancingv2=={CDK_VERSION}",
        f"aws-cdk.aws-iam=={CDK_VERSION}",
        f"aws-cdk.aws-lambda=={CDK_VERSION}",
        f"aws-cdk.aws-rds=={CDK_VERSION}",
        f"aws-cdk.aws-route53=={CDK_VERSION}",
        f"aws-cdk.aws-s3=={CDK_VERSION}",
        f"aws-cdk.aws-secretsmanager=={CDK_VERSION}",
        f"aws-cdk.aws-sns=={CDK_VERSION}",
        f"aws-cdk.aws-ssm=={CDK_VERSION}",
        f"aws-cdk.core=={CDK_VERSION}",
        f"oe-patterns-cdk-common@git+https://github.com/ordinaryexperts/aws-marketplace-oe-patterns-cdk-common@2.0.1"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
