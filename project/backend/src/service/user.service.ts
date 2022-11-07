import {Preference, User} from "../interface/interfaces";
import {BookModel, PreferenceModel, UserModel} from "../database/models";

export class UserService {

    static async getUser(id: number): Promise<User> {
        return (await UserModel.findOne({
            where: {
                id: id,
            },
            include: BookModel,
        }))?.toJSON() as User;
    }

    static async addUser(user: User): Promise<void> {
        delete user.id;

        await UserModel.create({
            ...user
        });
    }

    static async editUser(user: User): Promise<void> {
        delete user.id;

        await UserModel.create({
            ...user
        });
    }

    static async deleteUser(user: User): Promise<void> {
        await UserModel.destroy({
            where: {
                id: user.id,
            }
        });
    }

    static async addPreference(user: User, preference: Preference): Promise<void> {
        const userModel = await UserModel.findOne({
            where: {
                id: user.id,
            },
            include: PreferenceModel,
        });

        const preferenceModel = await PreferenceModel.findOne({
            where: {
                name: preference.name,
            }
        });

        // @ts-ignore
        userModel.addPreferenceModel(preferenceModel);
    }

    static async removePreference(user: User, preference: Preference): Promise<void> {
        const userModel = await UserModel.findOne({
            where: {
                id: user.id,
            },
            include: PreferenceModel,
        });

        const preferenceModel = await PreferenceModel.findOne({
            where: {
                name: preference.name,
            }
        });

        // @ts-ignore
        userModel.destroyPreferenceModel(preferenceModel);
    }

}